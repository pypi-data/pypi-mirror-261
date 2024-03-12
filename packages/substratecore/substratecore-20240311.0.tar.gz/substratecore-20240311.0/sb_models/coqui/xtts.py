"""
Original implementation reference: https://huggingface.co/spaces/coqui/xtts/blob/main/app.py
Includes a streaming example.
"""
import os
import time
from typing import Union, Optional
from pathlib import Path

from modal import (
    Stub,
    Image,
    Secret,
    NetworkFileSystem,
    gpu,
    method,
)

from sb_models.logger import log
from sb_models.network import save_wav, get_wav_seconds, handle_store_for_audio
from sb_models.usage_models import XTTSUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import GenerateSpeechOut

GPU_TYPE = gpu.A10G()
MODEL_ID = "tts_models/multilingual/multi-dataset/xtts_v2"
TMP_FILES = Path("/tmp/audio")
OUT_PATH = "/root/outs"
MODEL_FOLDER = "xtts"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)


def download_model():
    from TTS.utils.manage import ModelManager

    t0 = time.time()
    # NOTE: coqui has shut down, and modal released xtts, so this seems fine
    os.environ["COQUI_TOS_AGREED"] = "1"
    ModelManager().download_model(MODEL_ID)
    log.info(f"Downloaded {MODEL_ID} in {time.time() - t0:.2f}s")


image = (
    Image.from_registry(
        "nvidia/cuda:12.1.1-devel-ubuntu22.04",
        add_python="3.11",
    )
    .apt_install("git", "espeak", "ffmpeg")
    .pip_install(
        "torch==2.2.0",
        "torchaudio==2.2.0",
        # ran into this issue on 0.22.0 https://github.com/coqui-ai/TTS/issues/3462
        "TTS==0.21.3",
        "deepspeed==0.11.1",
        "pydub==0.25.1",
        "scipy",
        "numpy",
        "requests==2.28.1",
        "boto3==1.34.47",
    )
    .run_function(
        download_model,
        gpu="any",
        timeout=60 * 30,
    )
)

stub = Stub(name="xtts", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


@stub.cls(
    gpu=GPU_TYPE,
    timeout=60 * 5,
    container_idle_timeout=60 * 3,
    keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
    network_file_systems={OUT_PATH: assets_nfs},
    secrets=[
        Secret.from_name("aws-file-storage-key", environment_name="main"),
    ],
)
class XTTS:
    def __enter__(self) -> None:
        # import torch
        from TTS.tts.models.xtts import Xtts
        from TTS.utils.generic_utils import get_user_data_dir
        from TTS.tts.configs.xtts_config import XttsConfig

        t0 = time.time()
        model_path = os.path.join(get_user_data_dir("tts"), MODEL_ID.replace("/", "--"))

        config = XttsConfig()
        config.load_json(os.path.join(model_path, "config.json"))

        model = Xtts.init_from_config(config)
        model.load_checkpoint(
            config,
            checkpoint_path=os.path.join(model_path, "model.pth"),
            vocab_path=os.path.join(model_path, "vocab.json"),
            eval=True,
            use_deepspeed=True,
        )
        model.cuda()
        self.model = model
        log.info(f"Loaded models in {time.time() - t0:.2f}s.")

    @method()
    async def generate(
        self,
        text: str,
        audio_uri: Optional[str],
        store: Union[str, bool] = False,
        language: Optional[str] = "en",
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[GenerateSpeechOut, XTTSUsage]:
        import base64
        import hashlib
        from io import BytesIO

        import numpy as np
        from scipy.io import wavfile

        t0 = time.time()

        # TODO: think about this default speaker voice
        if not audio_uri:
            audio_uri = "https://cdn-uploads.huggingface.co/production/uploads/noauth/rHXF-_UHXJZOqQeQxMpwB.wav"

        # get the speaker file
        file_hash = hashlib.md5(f"{audio_uri}".encode("utf-8")).hexdigest()
        TMP_FILES.mkdir(parents=True, exist_ok=True)
        speaker_fp = TMP_FILES / file_hash
        input_audio_info = save_wav(audio_uri, speaker_fp, req=req)

        (
            gpt_cond_latent,
            speaker_embedding,
        ) = self.model.get_conditioning_latents(
            audio_path=speaker_fp, gpt_cond_len=30, gpt_cond_chunk_len=4, max_ref_length=60
        )
        speaker_latent_s = time.time() - t0
        log.info(f"Generated speaker latent in: {speaker_latent_s:.2f}s.")

        t0 = time.time()
        out = self.model.inference(
            text,
            language,
            gpt_cond_latent,
            speaker_embedding,
            repetition_penalty=5.0,
            temperature=0.75,
            enable_text_splitting=True,
        )
        gen_speech_s = time.time() - t0
        execution_s = speaker_latent_s + gen_speech_s
        log.info(f"Generated speech in: {gen_speech_s:.2f}s.")
        wav = out["wav"]
        samplerate = 24_000
        memfile = BytesIO()
        data = np.array(wav, dtype=np.float32)
        # Scale the float32 data to the range of int16
        scaled_data = np.int16(data / np.max(np.abs(data)) * 32767)
        wavfile.write(memfile, samplerate, scaled_data)
        memfile.seek(0)

        output_audio_seconds = get_wav_seconds(memfile)

        memfile.seek(0)
        wav_bytes = memfile.read()
        output_audio_bytes = len(wav_bytes)
        b64_wav = base64.b64encode(wav_bytes)

        uri = handle_store_for_audio(
            store, audio_b64=b64_wav, write_path=WRITE_PATH, model_folder=MODEL_FOLDER, req=req
        )

        usage = XTTSUsage(
            machine_config=str(GPU_TYPE),
            execution_seconds=execution_s,
            input_audio_bytes=input_audio_info.size_bytes,
            input_audio_seconds=input_audio_info.length_seconds,
            output_audio_bytes=output_audio_bytes,
            output_audio_seconds=output_audio_seconds,
        )
        return InferenceRun(result=GenerateSpeechOut(audio_uri=uri), usage=usage)


def encode_wav_to_base64(filepath) -> bytes:
    import base64

    with open(filepath, "rb") as wav_file:
        encoded_wav = base64.b64encode(wav_file.read())
    return encoded_wav


@stub.local_entrypoint()
async def main():
    import base64

    text = """The gods had condemned Sisyphus to ceaselessly rolling a rock to the top of a mountain, whence the stone would fall back of its own weight. They had thought with some reason that there is no more dreadful punishment than futile and hopeless labor.
    If one believes Homer, Sisyphus was the wisest and most prudent of mortals. According to another tradition, however, he was disposed to practice the profession of highwayman. I see no contradiction in this. Opinions differ as to the reasons why he became the futile laborer of the underworld. To begin with, he is accused of a certain levity in regard to the gods. He stole their secrets. Ægina, the daughter of Æsopus, was carried off by Jupiter. The father was shocked by that disappearance and complained to Sisyphus. He, who knew of the abduction, offered to tell about it on condition that Æsopus would give water to the citadel of Corinth. To the celestial thunderbolts he preferred the benediction of water. He was punished for this in the underworld. Homer tells us also that Sisyphus had put Death in chains. Pluto could not endure the sight of his deserted, silent empire. He dispatched the god of war, who liberated Death from the hands of her conqueror."""

    tts = XTTS()
    res = tts.generate.remote(
        # text="from chicago, to new york, i took the train.",
        text=text,
        audio_uri="https://cdn-uploads.huggingface.co/production/uploads/noauth/rHXF-_UHXJZOqQeQxMpwB.wav",
        # text="hola señor",
    )
    output_path = os.path.expanduser("~/Downloads/bark_test_out.wav")
    with open(output_path, "wb") as wav_file:
        wav_file.write(base64.b64decode(res.result.audio_uri))
