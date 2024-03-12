import time
import pathlib
from typing import Optional

from modal import (
    Dict,
    Stub,
    Image,
    Mount,
    gpu,
    method,
)

from sb_models.network import save_file
from sb_models.types.outputs import SeamlessOut
from sb_models.types.request import SubstrateRequest

MODEL_NAME = "seamless_expressivity"
VOCODER_NAME = "vocoder_pretssel"
AUDIO_SAMPLE_RATE = 16000
MAX_INPUT_AUDIO_LENGTH = 60  # seconds
CHECKPOINTS_PATH = pathlib.Path("/seamless-model")
GPU_TYPE = gpu.A100()


def download_model():
    from huggingface_hub import snapshot_download

    if not CHECKPOINTS_PATH.exists():
        snapshot_download(
            repo_id="facebook/seamless-expressive",
            repo_type="model",
            local_dir=CHECKPOINTS_PATH,
            token="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",
        )
        snapshot_download(
            repo_id="facebook/seamless-m4t-v2-large",
            repo_type="model",
            local_dir=CHECKPOINTS_PATH,
            token="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",
        )


image = (
    Image.from_registry(
        "nvidia/cuda:12.1.1-devel-ubuntu22.04",
        setup_dockerfile_commands=[
            "RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends git git-lfs wget curl build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev ffmpeg libsndfile-dev && apt-get clean && rm -rf /var/lib/apt/lists/*",
            "RUN pip install fairseq2 --pre --extra-index-url https://fair.pkg.atmeta.com/fairseq2/pt2.1.0/cu121",
        ],
        add_python="3.10",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .apt_install("git")
    .pip_install(
        "hf_transfer",
        "huggingface_hub",
        "omegaconf==2.3.0",
        "torch==2.1.1",
        "torchaudio==2.1.1",
    )
    .pip_install("git+https://github.com/facebookresearch/seamless_communication.git")
    .run_function(download_model)
)

stub = Stub("seamless")
stub.cache = Dict.new()

ENG_CODE = "eng"
DEU_CODE = "deu"

with image.run_inside():
    import tempfile

    import torch
    import torchaudio
    from fairseq2.data import Collater
    from fairseq2.assets import InProcAssetMetadataProvider, asset_store
    from fairseq2.memory import MemoryBlock
    from fairseq2.data.audio import (
        AudioDecoder,
        WaveformToFbankOutput,
        WaveformToFbankConverter,
    )
    from fairseq2.generation import NGramRepeatBlockProcessor
    from seamless_communication.inference import (
        Translator,
        SequenceGeneratorOptions,
    )
    from seamless_communication.models.unity import (
        load_gcmvn_stats,
        load_unity_unit_tokenizer,
    )
    from seamless_communication.cli.expressivity.evaluate.pretssel_inference_helper import (
        PretsselGenerator,
    )


mount_local = pathlib.Path(__file__).parent


@stub.cls(
    gpu=GPU_TYPE,
    mounts=[
        Mount.from_local_dir(mount_local, remote_path="/assets"),
    ],
    container_idle_timeout=60 * 20,
    image=image,
)
class Seamless:
    def __enter__(self):
        asset_store.env_resolvers.clear()
        asset_store.env_resolvers.append(lambda: "substrate")
        ip_meta = [
            {
                "name": "seamless_expressivity@substrate",
                "checkpoint": f"file://{CHECKPOINTS_PATH}/m2m_expressive_unity.pt",
                "char_tokenizer": f"file://{CHECKPOINTS_PATH}/spm_char_lang38_tc.model",
            },
            {
                "name": "vocoder_pretssel@substrate",
                "checkpoint": f"file://{CHECKPOINTS_PATH}/pretssel_melhifigan_wm-final.pt",
            },
            {
                "name": "seamlessM4T_v2_large@substrate",
                "checkpoint": f"file://{CHECKPOINTS_PATH}/seamlessM4T_v2_large.pt",
                "char_tokenizer": f"file://{CHECKPOINTS_PATH}/spm_char_lang38_tc.model",
            },
        ]

        asset_store.metadata_providers.append(InProcAssetMetadataProvider(ip_meta))
        if torch.cuda.is_available():
            device = torch.device("cuda:0")
            dtype = torch.float16
        else:
            device = torch.device("cpu")
            dtype = torch.float32
        self.m4t_translator = Translator(
            model_name_or_card="seamlessM4T_v2_large",
            vocoder_name_or_card=None,
            device=device,
            dtype=dtype,
        )
        unit_tokenizer = load_unity_unit_tokenizer(MODEL_NAME)
        _gcmvn_mean, _gcmvn_std = load_gcmvn_stats(VOCODER_NAME)
        self.gcmvn_mean = torch.tensor(_gcmvn_mean, device=device, dtype=dtype)
        self.gcmvn_std = torch.tensor(_gcmvn_std, device=device, dtype=dtype)

        self.translator = Translator(
            MODEL_NAME,
            vocoder_name_or_card=None,
            device=device,
            dtype=dtype,
            apply_mintox=False,
        )

        self.text_generation_opts = SequenceGeneratorOptions(
            beam_size=5,
            unk_penalty=torch.inf,
            soft_max_seq_len=(0, 200),
            step_processor=NGramRepeatBlockProcessor(
                ngram_size=10,
            ),
        )
        self.m4t_text_generation_opts = SequenceGeneratorOptions(
            beam_size=5,
            unk_penalty=torch.inf,
            soft_max_seq_len=(1, 200),
            step_processor=NGramRepeatBlockProcessor(
                ngram_size=10,
            ),
        )

        self.pretssel_generator = PretsselGenerator(
            VOCODER_NAME,
            vocab_info=unit_tokenizer.vocab_info,
            device=device,
            dtype=dtype,
        )

        self.decode_audio = AudioDecoder(dtype=torch.float32, device=device)

        self.convert_to_fbank = WaveformToFbankConverter(
            num_mel_bins=80,
            waveform_scale=2**15,
            channel_last=True,
            standardize=False,
            device=device,
            dtype=dtype,
        )
        self.collate = Collater(pad_value=0, pad_to_multiple=1)

    @method()
    def run(
        self,
        input_audio: str,
        source_language_code: str = ENG_CODE,
        target_language_code: str = DEU_CODE,
        use_hosted: Optional[bool] = False,
        req: Optional[SubstrateRequest] = None,
    ) -> SeamlessOut:
        # input_audio is either base64 encoded or a path to a wav file
        if input_audio.startswith("data:audio/wav;base64,"):
            import base64

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fi:
                fi.write(base64.b64decode(input_audio[22:]))
                input_audio_path = fi.name
        # if it is a remote url:
        elif input_audio.startswith("http"):
            import hashlib

            file_hash = hashlib.md5(f"{input_audio}".encode("utf-8")).hexdigest() + ".wav"
            fp = pathlib.Path("/tmp") / file_hash
            save_file(input_audio, fp, req=req)
            input_audio_path = str(fp)
        else:
            input_audio_path = input_audio

        preprocess_audio(input_audio_path)

        with pathlib.Path(input_audio_path).open("rb") as fb:
            block = MemoryBlock(fb.read())
            example = self.decode_audio(block)

        example = self.convert_to_fbank(example)
        example = normalize_fbank(example, self.gcmvn_mean, self.gcmvn_std)
        example = self.collate(example)
        source_sentences, _ = self.m4t_translator.predict(
            input=example["fbank"],
            task_str="S2TT",  # get source text
            tgt_lang=source_language_code,
            text_generation_opts=self.m4t_text_generation_opts,
        )
        source_text = str(source_sentences[0])

        prosody_encoder_input = example["gcmvn_fbank"]
        text_output, unit_output = self.translator.predict(
            example["fbank"],
            "S2ST",
            tgt_lang=target_language_code,
            src_lang=source_language_code,
            text_generation_opts=self.text_generation_opts,
            unit_generation_ngram_filtering=False,
            duration_factor=1.0,
            prosody_encoder_input=prosody_encoder_input,
            src_text=source_text,  # for mintox check
        )
        speech_output = self.pretssel_generator.predict(
            unit_output.units,
            tgt_lang=target_language_code,
            prosody_encoder_input=prosody_encoder_input,
        )

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            torchaudio.save(
                f.name,
                speech_output.audio_wavs[0][0].to(torch.float32).cpu(),
                sample_rate=speech_output.sample_rate,
            )

        text_out = remove_prosody_tokens_from_text(str(text_output[0]))

        return SeamlessOut(audio_uri=encode_wav_to_base64(f.name), text=text_out)


def encode_wav_to_base64(filepath) -> bytes:
    import base64

    with open(filepath, "rb") as wav_file:
        encoded_wav = base64.b64encode(wav_file.read())
    return encoded_wav


def normalize_fbank(data: "WaveformToFbankOutput", gcmvn_mean, gcmvn_std) -> "WaveformToFbankOutput":
    fbank = data["fbank"]
    std, mean = torch.std_mean(fbank, dim=0)
    data["fbank"] = fbank.subtract(mean).divide(std)
    data["gcmvn_fbank"] = fbank.subtract(gcmvn_mean).divide(gcmvn_std)
    return data


def remove_prosody_tokens_from_text(text):
    # filter out prosody tokens, there is only emphasis '*', and pause '='
    text = text.replace("*", "").replace("=", "")
    text = " ".join(text.split())
    return text


def preprocess_audio(input_audio_path: str) -> None:
    arr, org_sr = torchaudio.load(input_audio_path)
    new_arr = torchaudio.functional.resample(arr, orig_freq=org_sr, new_freq=AUDIO_SAMPLE_RATE)
    max_length = int(MAX_INPUT_AUDIO_LENGTH * AUDIO_SAMPLE_RATE)
    if new_arr.shape[1] > max_length:
        new_arr = new_arr[:, :max_length]
    torchaudio.save(input_audio_path, new_arr, sample_rate=AUDIO_SAMPLE_RATE)


TARGET_LANGUAGE_NAMES = [
    "English",
    "French",
    "German",
    "Spanish",
]


@stub.local_entrypoint()
def test():
    import base64

    # encoded = encode_wav_to_base64(
    #     "/Users/robcheung/code/substrate/sb_models/seamless/assets_Sad-English.wav"
    # )
    # # to string with data:audio/wav;base64,
    # encoded_str = "data:audio/wav;base64," + encoded.decode("utf-8")

    res = Seamless().run.remote(
        # "https://huggingface.co/spaces/facebook/seamless-m4t-v2-large/resolve/main/assets/sample_input_2.mp3",
        "https://huggingface.co/spaces/facebook/seamless-expressive/resolve/main/assets/Excited-English.wav",
        # encoded_str,
        target_language_code="cmn",
    )
    with open(f"/tmp/seamless-test-{int(time.time())}.wav", "wb") as wav_file:
        wav_file.write(base64.b64decode(res.audio_uri))
