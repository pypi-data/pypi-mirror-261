import os
import time
import asyncio
import hashlib
import mimetypes
from typing import List, Optional
from pathlib import Path

from modal import Stub, Image, Secret, Function, gpu, method

from sb_models.logger import log
from sb_models.network import save_file
from sb_models.usage_models import WhisperUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import ChapterMarker, TranscribedWord, TranscribedSegment, TranscribeMediaOut

URL_DOWNLOADS_DIR = Path("/tmp/url_downloads")
TMP_FILES = Path("/tmp/audio")

GPU_TYPE = gpu.A10G()
DEVICE = "cuda"
BATCH_SIZE = 24
MODEL_NAME = "large-v3"
MODEL_DIR = "/model"


def download_models():
    """
    Download models, mainly from huggingface. This method is only called
    in the build phase of the image in order to "bake" the weights directly
    in to the image vs. using an e.g. shared volume, which would be slower at
    inference
    """
    t0 = time.time()
    import whisperx

    default_models = whisperx.alignment.DEFAULT_ALIGN_MODELS_TORCH
    community_models = whisperx.alignment.DEFAULT_ALIGN_MODELS_HF
    all_alignment_models = default_models | community_models
    for model in all_alignment_models:
        whisperx.load_align_model(language_code=model, device=DEVICE, model_dir=MODEL_DIR)
    hf_token = os.environ["HUGGINGFACE_TOKEN"]
    whisperx.DiarizationPipeline(use_auth_token=hf_token, device=DEVICE)

    log.info(f"Downloaded models (with {len(all_alignment_models)} alignments) in {time.time() - t0:.2f}s")


def warm_up():
    import whisperx

    audio_url = "https://media.substrate.run/chess.mp3"
    file_hash = hashlib.md5(f"{audio_url}".encode("utf-8")).hexdigest()
    TMP_FILES.mkdir(parents=True, exist_ok=True)
    fp = TMP_FILES / file_hash

    save_file(audio_url, fp)
    t0 = time.time()
    pipeline = whisperx.load_model(
        MODEL_NAME,
        device=DEVICE,
        compute_type="float16",
        asr_options={"compression_ratio_threshold": 2},
    )
    audio = whisperx.load_audio(str(fp))
    pipeline.transcribe(audio, batch_size=BATCH_SIZE)
    log.info(f"DOWNLOAD WARMUP {time.time() - t0:.2f}s")


app_image = (
    Image.from_registry(
        "nvidia/cuda:12.1.1-devel-ubuntu22.04",
        add_python="3.10",
    )
    .apt_install("ffmpeg", "git", "curl")
    .pip_install(
        "git+https://github.com/SubstrateLabs/whisperx.git@main",
        "git+https://github.com/yt-dlp/yt-dlp.git@master",
    )
    .run_function(
        download_models,
        timeout=60 * 30,
        gpu="any",
        secrets=[Secret.from_name("huggingface-secret", environment_name="main")],
    )
    .pip_install("ffmpeg-python==0.2.0")
    .apt_install("libcublas11")
    .pip_install("torch==2.2.0", "torchaudio==2.2.0", index_url="https://download.pytorch.org/whl/cu121")
    .run_function(warm_up, gpu="A10G")
    .run_commands(
        "python -m pytorch_lightning.utilities.upgrade_checkpoint /root/.cache/torch/whisperx-vad-segmentation.bin",
        gpu="any",
    )
)

stub = Stub("whisper", image=app_image)


@stub.cls(
    gpu=GPU_TYPE,
    timeout=60 * 8,  # 8 minutes max per input
    container_idle_timeout=60 * 3,
    secrets=[Secret.from_name("huggingface-secret", environment_name="main")],
    keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
)
class Transcriber:
    def __enter__(self) -> None:
        import whisperx

        t0 = time.time()
        self.pipeline = whisperx.load_model(
            MODEL_NAME,
            device=DEVICE,
            compute_type="float16",
            asr_options={"compression_ratio_threshold": 2},
        )
        default_models = whisperx.alignment.DEFAULT_ALIGN_MODELS_TORCH
        community_models = whisperx.alignment.DEFAULT_ALIGN_MODELS_HF
        self.all_alignment_models = default_models | community_models
        self.alignment_models = {}
        log.info(f"Loaded models in {time.time() - t0:.2f}s.")

    @staticmethod
    async def chapter_runner(segments) -> List[ChapterMarker]:
        from pydantic import BaseModel

        t0 = time.time()

        class ChapterList(BaseModel):
            chapters: List[ChapterMarker]

        SYSTEM = """
        Please provide a list of chapters for the following transcript. 
        Make sure to think step by step. 
        First, think about the most important topics in the transcript and list them out in the order they appear. 
        Then, think about how you would divide the transcript into chapters based on these topics. 
        Finally, think about how you would title each chapter and what timecode it starts at.

        Make sure to meet these constraints:
        - The chapters should cover only the key points and main ideas presented in the original transcript
        - Please ensure the time of the chapter is marked as when the topic is first introduced based on the times you have been given as numbers
        - The chapters should focus on macro-level topics, not micro-level details. This is very important. I cannot stress this enough.
        - The chapters should be fairly evenly spaced throughout time. Don't put two chapters at the same timecode
        - Do not forget to add the start time of the chapter as a float in seconds to each chapter
        - Chapter titles should fit the tone of the content itself
        - Be concise, and keep the chapter titles short and descriptive.
        
        Inputs will be in the format
        [start time second]: [text]
        e.g.
        
        [59.73] Hello I'm going to talk about some topic
        
        Where the start time is 59.73 seconds.

        Respond with the following JSON schema for chapters:
        - title: title of the chapter
        - start_time: start time of the chapter as a float in seconds. do not forget this field
        """

        json_schema = ChapterList.schema_json()
        fn = Function.lookup("mistral-7b-instruct", "Mistral.generate")
        texts = [f"[{s.get('start')}] {s.get('text')}" for s in segments]
        segments_str = "\n".join(texts)

        max_num_tokens = 4200
        max_num_words = 3 * (max_num_tokens / 4)
        should_split = segments_str.count(" ") > max_num_words
        if should_split:
            messages = []
            current_message = ""
            for segment in segments:
                if current_message.count(" ") > max_num_words:
                    messages.append(current_message)
                    current_message = ""
                current_message += f"[{segment['start']}] {segment['text']}\n"
            messages.append(current_message)

            log.info(f"split transcript into {len(messages)} messages")
            chapters = []

            runs = await asyncio.gather(
                *[
                    fn.remote.aio(
                        system=SYSTEM,
                        prompts=[{"prompt": "Transcript:\n" + message}],
                        json_schema=json_schema,
                        temperature=0.2,
                        max_tokens=2400,
                    )
                    for message in messages
                ]
            )
            for r in runs:
                for res in r.result:
                    cc = res.json_completions[0]["chapters"]
                    chapters.extend(cc)

            CONSOLIDATE_PROMPT = """
            Please consolidate this chapter list into a single list of chapters.
            Never drop any distinct chapters, but you can delete duplicates. If timestamps are close and the chapter titles are similar, you can collapse them. 

            Each chapter should have the following fields:
            - title: title of the chapter
            - start_time: start time of the chapter as a float in seconds
            """

            chap_list = [{"title": c.get("title"), "start_time": c.get("start_time")} for c in chapters]
            chap_list = sorted(chap_list, key=lambda x: x.get("start_time", 0) or 0)

            chapters_str = "\n".join([f"{chapter['start_time']}: {chapter['title']}" for chapter in chap_list])

            run = await fn.remote.aio(
                system=CONSOLIDATE_PROMPT,
                prompts=[{"prompt": f"Chapters:\n{chapters_str}"}],
                json_schema=json_schema,
                temperature=0.1,
                max_tokens=2400,
            )
            final_res = run.result

        else:
            log.info("not splitting")
            run = await fn.remote.aio(
                system=SYSTEM,
                prompts=[{"prompt": "Transcript:\n" + segments_str}],
                json_schema=json_schema,
                temperature=0.1,
                max_tokens=1200,
                frequency_penalty=0.1,
                presence_penalty=1.1,
                repetition_penalty=1.0,
            )
            final_res = run.result
        final_chapters = final_res[0].json_completions[0]["chapters"]
        log.info(f"{len(final_chapters)} Chapters generated in {time.time() - t0:.2f}s")
        return final_chapters

    @method()
    async def transcribe(
        self,
        audio_url: str,
        align: Optional[bool] = False,
        prompt: Optional[str] = None,
        language: Optional[str] = "en",
        diarize: Optional[bool] = False,
        return_segments: Optional[bool] = False,
        suggest_chapters: Optional[bool] = False,
        chunk_size: Optional[int] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[TranscribeMediaOut, WhisperUsage]:
        import gc

        import torch
        import ffmpeg
        import whisperx

        t0 = time.time()
        file_hash = hashlib.md5(f"{audio_url}".encode("utf-8")).hexdigest()
        TMP_FILES.mkdir(parents=True, exist_ok=True)
        fp = TMP_FILES / file_hash

        input_bytes = save_file(audio_url, fp, req=req)
        mime_type, _ = mimetypes.guess_type(fp)
        media_type = "audio"
        if mime_type:
            guess = mime_type.split("/")[0]
            if guess in ["audio", "video"]:
                media_type = guess

        is_video = media_type == "video"
        if is_video:
            mp3_fp = TMP_FILES / f"{file_hash}.mp3"
            input_stream = ffmpeg.input(fp)
            output_stream = ffmpeg.output(input_stream, str(mp3_fp))
            ffmpeg.run(output_stream)
            fp = mp3_fp

        probe = ffmpeg.probe(fp)
        input_seconds = float(probe["format"]["duration"])
        self.pipeline.options = self.pipeline.options._replace(initial_prompt=prompt)

        chunk_size = chunk_size or 30
        audio = whisperx.load_audio(str(fp))
        transcript_result = self.pipeline.transcribe(
            audio, batch_size=BATCH_SIZE, language=language, chunk_size=chunk_size
        )
        full_text = " ".join([s["text"] for s in transcript_result["segments"]])
        tokenizer = self.pipeline.model.hf_tokenizer

        token_count = len(tokenizer.encode(full_text))
        diff = time.time() - t0
        log.info(f"Transcribed in {diff:.2f}s @ {token_count / diff:.2f} tok/s")

        chapters = None
        if suggest_chapters:
            chapters = await Transcriber.chapter_runner(transcript_result["segments"])

        if align:
            align_code = (
                transcript_result["language"]
                if transcript_result.get("language") in self.all_alignment_models
                else "en"
            )
            t2 = time.time()
            if align_code in self.alignment_models:
                model_a, meta = self.alignment_models[align_code]
            else:
                model_a, meta = whisperx.load_align_model(
                    None,
                    model_name=self.all_alignment_models[align_code],
                    device=DEVICE,
                    model_dir=MODEL_DIR,
                )
                self.alignment_models[align_code] = (model_a, meta)
            aligned = whisperx.align(
                transcript_result["segments"],
                model_a,
                meta,
                audio,
                DEVICE,
                return_char_alignments=False,
                include_scores=False,
            )
            gc.collect()
            torch.cuda.empty_cache()
            if align_code != "en":
                del model_a
                del self.alignment_models[align_code]
            log.info(f"Aligned in {time.time() - t2:.2f}s")
            transcript_result["segments"] = aligned["segments"]
            transcript_result["word_segments"] = aligned["word_segments"]

        if diarize:
            if audio is None:
                audio = whisperx.load_audio(str(fp))
            hf_token = os.environ["HUGGINGFACE_TOKEN"]
            diarize_model = whisperx.DiarizationPipeline(use_auth_token=hf_token, device=DEVICE)

            t3 = time.time()
            diarize_df = diarize_model(audio, min_speakers=1, max_speakers=4)
            log.info(f"Diarized in {time.time() - t3:.2f}s")
            transcript_result = whisperx.assign_word_speakers(diarize_df, transcript_result)

        execution_s = time.time() - t0
        log.info(f"Finished transcribe in {execution_s:.2f}s")
        results: List[TranscribedSegment] = []
        segments = None
        if align or return_segments:
            segments = transcript_result.get("segments")
            for segment in segments:
                word_segments = segment.get("words")
                words = (
                    [
                        TranscribedWord(
                            word=w.get("word"),
                            start=w.get("start"),
                            end=w.get("end"),
                            speaker=w.get("speaker"),
                        )
                        for w in word_segments
                        if w.get("word")
                    ]
                    if word_segments
                    else None
                )
                segment_model = TranscribedSegment(
                    text=segment["text"],
                    start=segment["start"],
                    end=segment["end"],
                    speaker=segment.get("speaker"),
                    words=words,
                )
                results.append(segment_model)

        usage = WhisperUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            input_audio_bytes=input_bytes,
            input_audio_seconds=input_seconds,
            diarize_enabled=diarize or False,
            align_enabled=align or False,
            chapters_enabled=suggest_chapters or False,
            output_segment_count=len(segments) if segments else 0,
        )

        result = TranscribeMediaOut(text=full_text, segments=results, chapters=chapters)
        return InferenceRun(result=result, usage=usage)


@stub.local_entrypoint()
async def main():
    # url = "https://media.substrate.run/dfw-10m.mp3"
    # url = "https://media.substrate.run/dfw-interview.m4a"
    # url = "https://media.substrate.run/chess.mp3"
    url = "https://substack-video-staging.s3.amazonaws.com/video_upload/post/4356/fd446936-a8b7-4ee9-8ed9-0c5cb26fe60e/transcoded.mp3?AWSAccessKeyId=AKIA6ANP2FN4V3IHWAXW&Signature=lZOX6fPSNTeFCoXWi8GqreuP6As%3D&Expires=1708551644"
    res = Transcriber().transcribe.remote(
        audio_url=url,
        align=True,
        diarize=True,
        suggest_chapters=True,
        # prompt="Transcript of a video titled: Analysis of my match against Harika Dronavalli",
    )
    log.info(res.result.dict())
    # for s in res.result:
    #     log.info(s.text)
