import os

from modal import Stub, Image, Secret, method

from sb_models.logger import log


def download_model():
    from huggingface_hub import snapshot_download

    snapshot_download(
        "meta-llama/Llama-2-13b-chat-hf",
        local_dir="/model",
        token=os.environ["HUGGINGFACE_TOKEN"],
    )


MODEL_DIR = "/model"

# Dockerhub image recommended by `vLLM`, then upgrade the torch version to one specifically built for CUDA 11.8.
image = (
    Image.from_registry("nvcr.io/nvidia/pytorch:22.12-py3")
    .pip_install("torch==2.0.1", index_url="https://download.pytorch.org/whl/cu118")
    .pip_install("vllm @ git+https://github.com/vllm-project/vllm.git@bda41c70ddb124134935a90a0d51304d2ac035e8")
    .pip_install("hf-transfer~=0.1")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        download_model,
        secret=Secret.from_name("huggingface-secret", environment_name="main"),
        timeout=60 * 20,
    )
)

stub = Stub("llama-13b", image=image)


@stub.cls(gpu="A100", secret=Secret.from_name("huggingface-secret", environment_name="main"))
class Model:
    def __enter__(self):
        from vllm import LLM

        self.llm = LLM(MODEL_DIR)
        self.template = """SYSTEM: You are a helpful assistant.
USER: {}
ASSISTANT: """

    @method()
    def generate(self, user_questions):
        from vllm import SamplingParams

        prompts = [self.template.format(q) for q in user_questions]
        sampling_params = SamplingParams(
            temperature=0.75,
            top_p=1,
            max_tokens=800,
            presence_penalty=1.15,
        )
        results = self.llm.generate(prompts, sampling_params)
        num_tokens = 0
        responses = []
        for output in results:
            num_tokens += len(output.outputs[0].token_ids)
            responses.append(output.outputs[0].text)
        log.info(f"Generated {num_tokens} tokens, {len(results)} results.")
        return responses


# todo
# @stub.function(timeout=60 * 10)
# @web_endpoint()
# def get(q: str):
#     from itertools import chain
#
#     from fastapi.responses import StreamingResponse
#
#     model = Model()
#     return StreamingResponse(
#         chain(
#             ("Loading...\n\n"),
#             model.generate.call([q]),
#         ),
#         media_type="text/event-stream",
#     )


@stub.local_entrypoint()
def main():
    model = Model()
    questions = ["Implement a Python function to compute the Fibonacci numbers."]
    model.generate.call(questions)
