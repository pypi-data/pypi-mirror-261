import os
import time
import base64
import hashlib
from io import BytesIO
from pathlib import Path

import numpy as np
import requests
from ray import serve
from fastapi import FastAPI
from scipy.io import wavfile
from TTS.utils.manage import ModelManager
from TTS.tts.models.xtts import Xtts
from TTS.tts.configs.xtts_config import XttsConfig

from sb_models import logger
from sb_models.substratecore.models import GenerateSpeechIn

TMP_FILES = Path("/cache")
MODEL_ID = "tts_models/multilingual/multi-dataset/xtts_v2"

app = FastAPI()


def download_model(model_path: str):
    t0 = time.time()
    # NOTE: coqui has shut down, and modal released xtts, so this seems fine
    os.environ["COQUI_TOS_AGREED"] = "1"
    if not os.path.exists(model_path):
        model_manager = ModelManager(output_prefix="/cache")
        model_manager.download_model(MODEL_ID)
        logger.log.info(f"Downloaded {MODEL_ID} in {time.time() - t0:.2f}s")
    else:
        logger.log.info("Model already downloaded. Using cached model.")


@serve.deployment(ray_actor_options={"num_gpus": 1})
@serve.ingress(app)
class XTTSModel:
    def __init__(self):
        t0 = time.time()
        model_path = os.path.join("/cache", "tts", MODEL_ID.replace("/", "--"))
        download_model(model_path)

        config = XttsConfig()
        config.load_json(os.path.join(model_path, "config.json"))

        model = Xtts.init_from_config(config)
        model.load_checkpoint(
            config,
            checkpoint_path=os.path.join(model_path, "model.pth"),
            vocab_path=os.path.join(model_path, "vocab.json"),
            eval=True,
            # use_deepspeed=True,
        )
        model.cuda()
        self.model = model
        self.log = logger.log.getChild("XTTSModel")
        self.log.info(f"Loaded models in {time.time() - t0:.2f}s.")

    @app.post("/")
    async def post(
        self,
        req: GenerateSpeechIn,
    ):
        audio_uri = req.audio_uri
        text = req.text
        language = req.language if req.language else "en"
        # TODO: think about this default speaker voice
        if not audio_uri:
            audio_uri = "https://cdn-uploads.huggingface.co/production/uploads/noauth/rHXF-_UHXJZOqQeQxMpwB.wav"

        # get the speaker file
        file_hash = hashlib.md5(f"{audio_uri}".encode("utf-8")).hexdigest()
        TMP_FILES.mkdir(parents=True, exist_ok=True)
        speaker_fp = TMP_FILES / file_hash
        with open(speaker_fp, "wb") as f:
            f.write(requests.get(audio_uri).content)
        # network.save_file(audio_uri, speaker_fp)

        t0 = time.time()
        (
            gpt_cond_latent,
            speaker_embedding,
        ) = self.model.get_conditioning_latents(
            audio_path=speaker_fp, gpt_cond_len=30, gpt_cond_chunk_len=4, max_ref_length=60
        )
        self.log.info(f"Generated speaker latent in: {time.time() - t0:.2f}s.")

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
        # token_count = self.model.tokenizer.get_number_tokens()
        self.log.info(f"Generated speech in: {time.time() - t0:.2f}s.")
        wav = out["wav"]
        samplerate = 24_000
        memfile = BytesIO()
        data = np.array(wav, dtype=np.float32)
        wavfile.write(memfile, samplerate, data)
        memfile.seek(0)
        wav_bytes = memfile.read()
        b64_wav = base64.b64encode(wav_bytes)
        return b64_wav


# def encode_wav_to_base64(filepath) -> bytes:
#     with open(filepath, "rb") as wav_file:
#         encoded_wav = base64.b64encode(wav_file.read())
#     return encoded_wav


xtts = XTTSModel.bind()
