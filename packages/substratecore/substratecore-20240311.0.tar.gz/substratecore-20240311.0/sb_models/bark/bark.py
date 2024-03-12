import os
import time
from typing import Optional

from modal import Stub, Image, gpu

from sb_models.logger import log
from sb_models.types.request import SubstrateRequest

GPU = gpu.A10G()
SPEAKER = "v2/en_speaker_9"

test_script = """The gods had condemned Sisyphus to ceaselessly rolling a rock to the top of a mountain, whence the stone would fall back of its own weight. They had thought with some reason that there is no more dreadful punishment than futile and hopeless labor.
If one believes Homer, Sisyphus was the wisest and most prudent of mortals. According to another tradition, however, he was disposed to practice the profession of highwayman. I see no contradiction in this. Opinions differ as to the reasons why he became the futile laborer of the underworld. To begin with, he is accused of a certain levity in regard to the gods. He stole their secrets. Ægina, the daughter of Æsopus, was carried off by Jupiter. The father was shocked by that disappearance and complained to Sisyphus. He, who knew of the abduction, offered to tell about it on condition that Æsopus would give water to the citadel of Corinth. To the celestial thunderbolts he preferred the benediction of water. He was punished for this in the underworld. Homer tells us also that Sisyphus had put Death in chains. Pluto could not endure the sight of his deserted, silent empire. He dispatched the god of war, who liberated Death from the hands of her conqueror."""
MODEL_ID = "suno/bark"
SAMPLE_RATE = 24_000


def download_model():
    import nltk
    import torch
    from transformers import BarkModel
    from huggingface_hub import snapshot_download
    from optimum.bettertransformer import BetterTransformer

    snapshot_download(MODEL_ID)
    model = BarkModel.from_pretrained("suno/bark", torch_dtype=torch.float16).to("cuda")
    BetterTransformer.transform(model, keep_original_model=False)

    nltk.download("punkt")


image = (
    Image.debian_slim("3.11")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .apt_install("git")
    .pip_install(
        "hf_transfer",
        "huggingface_hub==0.16.4",
        "tqdm",
        "nltk",
        "numpy",
        "scipy",
        "transformers==4.32.1",
        "torch==2.0.1",
        "accelerate==0.22.0",
        "safetensors==0.3.3",
        "optimum==1.12.0",
    )
    .run_function(download_model, gpu=GPU, timeout=60 * 30)
)

stub = Stub(name="bark", image=image)
web_img = Image.debian_slim().pip_install("scipy", "numpy")


@stub.function(image=image, gpu=GPU, timeout=60 * 10)
def tts_single(script: str, speaker):
    import torch
    from transformers import BarkModel, AutoProcessor
    from optimum.bettertransformer import BetterTransformer

    processor = AutoProcessor.from_pretrained("suno/bark", local_files_only=True)
    t0 = time.time()
    model = BarkModel.from_pretrained("suno/bark", torch_dtype=torch.float16, local_files_only=True).to("cuda")
    log.info(f"Loaded model in {time.time() - t0:.2f}s")
    model = BetterTransformer.transform(model)
    encoded_inputs = processor(script, voice_preset=speaker).to("cuda")
    token_count = torch.nonzero(encoded_inputs["input_ids"]).size(dim=0)
    t1 = time.time()
    audio_array = model.generate(**encoded_inputs)
    log.info(f"Generated audio in {time.time() - t1:.2f}s")
    return {
        "result": audio_array.cpu().numpy().squeeze().tolist(),
        "token_count": token_count,
    }


@stub.function(image=image, gpu=GPU, timeout=60 * 10)
def tts(
    script: str,
    speaker: str = SPEAKER,
    req: Optional[SubstrateRequest] = None,
):
    import nltk
    import numpy as np

    sentences = nltk.sent_tokenize(script)
    log.info(f"split into {len(sentences)} chunks")
    silence = np.zeros(int(0.25 * SAMPLE_RATE))

    pieces = []
    token_count = 0
    for output in tts_single.starmap([(sentence, speaker) for sentence in sentences]):
        pieces += [np.array(output["result"]), silence.copy()]
        token_count += output["token_count"]

    pieces = np.concatenate(pieces)
    return {"result": pieces.tolist(), "token_count": token_count}


@stub.local_entrypoint()
def run_local():
    import numpy as np
    import scipy

    output_path = os.path.expanduser("~/Downloads/bark_test_out.wav")
    output = tts.remote(test_script, "v2/en_speaker_6")
    ary = output["result"]
    ct = output["token_count"]
    log.info(f"token count: {ct}, len: {len(ary)}")
    scipy.io.wavfile.write(output_path, rate=SAMPLE_RATE, data=np.array(ary))
