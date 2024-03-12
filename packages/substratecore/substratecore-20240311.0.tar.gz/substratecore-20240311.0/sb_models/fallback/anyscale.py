import os
import json
import asyncio
from typing import Any, Dict, List, Union, Optional

from modal import Dict as ModalDict, Function

from sb_models.logger import log
from sb_models.usage_models import MistralUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.deprecated_models import (
    MistralPrompt,
    MistralResult,
)

ENABLE_ANYSCALE_FALLBACK = True

SYSTEM_MESSAGE = {"role": "system", "content": "You are a helpful AI assistant"}
SYSTEM_MESSAGE_JSON = {
    "role": "system",
    "content": "You are a helpful assistant that outputs in JSON. Be concise and follow instructions carefully",
}
MISTRAL_MAX_TOKENS = 12_000
TOKENIZER_MODEL = "mistralai/Mistral-7B-v0.1"


def resolve_ref(schema, definitions):
    """Recursively resolve $ref references in the schema."""
    if isinstance(schema, dict):
        if "$ref" in schema:
            ref_name = schema["$ref"].split("/")[-1]
            return resolve_ref(definitions.get(ref_name, {}), definitions)
        else:
            return {k: resolve_ref(v, definitions) for k, v in schema.items()}
    elif isinstance(schema, list):
        return [resolve_ref(item, definitions) for item in schema]
    else:
        return schema


def extract_schema(json_schema):
    as_dict = json.loads(json_schema) if isinstance(json_schema, str) else json_schema
    definitions = as_dict.get("definitions", {})
    if "$ref" in as_dict:
        ref_name = as_dict["$ref"].split("/")[-1]
        resolved_schema = resolve_ref({"$ref": f"#/definitions/{ref_name}"}, definitions)
        return resolved_schema
    else:
        return as_dict


async def _run_mistral_anyscale(
    prompt: Dict[str, Any],
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    num_completions: Optional[int] = None,
    json_schema: Optional[str] = None,
    # Extra args
    system="",
    presence_penalty: Optional[float] = None,
    frequency_penalty: Optional[float] = None,
    repetition_penalty: float = 1.0,
    top_p: Optional[float] = None,
    req: Optional[SubstrateRequest] = None,
) -> Union[InferenceRun[List[MistralResult], MistralUsage], None]:
    import time

    import aiohttp
    from transformers import AutoTokenizer

    t0 = time.time()
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"
    prompt_arg = MistralPrompt(**prompt)
    input_prompt = prompt_arg.prompt
    dd = Function.lookup("datadog", "log_event")
    token = os.getenv("ANYSCALE_API_KEY", None)
    if not token:
        log.error("Missing ANYSCALE API token.")
        return None

    try:
        async with aiohttp.ClientSession() as session:
            api_base = "https://api.endpoints.anyscale.com/v1"
            url = f"{api_base}/chat/completions"
            results = []
            token_count = 0
            input_token_count = 0
            tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_MODEL)
            tokens = tokenizer(
                input_prompt,
                return_tensors=None,
                max_length=MISTRAL_MAX_TOKENS,
                truncation=True,
            )
            truncated = tokenizer.decode(tokens["input_ids"], skip_special_tokens=True)
            body = {
                "model": model_name,
                "messages": [
                    SYSTEM_MESSAGE_JSON if json_schema else SYSTEM_MESSAGE,
                    {"role": "user", "content": truncated},
                ],
                "temperature": temperature,
                "presence_penalty": presence_penalty,
                "frequency_penalty": frequency_penalty,
                "max_tokens": max_tokens,
                "top_p": top_p,
            }
            if json_schema:
                as_dict = extract_schema(json_schema)
                if as_dict:
                    body["response_format"] = {
                        "type": "json_object",
                        "schema": as_dict,
                    }
                    body["top_p"] = 1

            completions = None
            json_completions = None
            headers = {"Authorization": f"Bearer {token}"}
            async with session.post(url, headers=headers, json=body) as resp:
                if resp.status == 200:
                    json_resp = await resp.json()
                    if json_schema:
                        json_completions = []
                        for c in json_resp["choices"]:
                            try:
                                parsed = json.loads(c["message"]["content"])
                            except Exception:
                                log.error("Failed to parse JSON")
                                parsed = c["message"]["content"]
                            if isinstance(parsed, str):
                                try:
                                    parsed = json.loads(parsed + '"}')
                                except Exception as e:
                                    log.error("Failed to parse JSON with curly")
                                    raise Exception("Failed to parse JSON") from e
                            json_completions.append(parsed)
                    else:
                        completions = [c["message"]["content"] for c in json_resp["choices"]]
                    results.append(
                        MistralResult(
                            completions=completions,
                            json_completions=json_completions,
                        )
                    )
                    token_count += json_resp["usage"]["completion_tokens"]
                    input_token_count += json_resp["usage"]["prompt_tokens"]
                else:
                    json_resp = await resp.json()
                    log.error(f"Failed to get completions: {resp.status}, {resp}, {json_resp}")
                    import copy

                    b = copy.deepcopy(body)
                    del b["messages"]
                    log.error(f"Request body: {b}")
                    raise Exception("Inference failed")

            dd.spawn(
                message="SUCCESS: mistral-7b fallback",
                name="mistral-7b-fallback-success",
                attributes=dict(
                    token_count=token_count,
                    input_token_count=input_token_count,
                    prompt_count=1,
                ),
            )
            execution_s = time.time() - t0
            usage = MistralUsage(
                execution_seconds=execution_s,
                machine_config="Vendor",
                output_token_count=token_count,
                input_token_count=input_token_count,
            )
            return InferenceRun(
                result=results,
                usage=usage,
            )
    except Exception as e:
        log.error(f"Failed to get completions: {e}")
        return None


async def execute_anyscale_fallback(fn, args, req) -> Union[InferenceRun[List[MistralResult], MistralUsage], None]:
    """
    Try to use anyscale to run Mistral. This can return None in a few of scenarios:
    - The anyscale API is down
    - We are at our anyscale concurrency limit
    - The json object that we get back is not parseable, even after some manual modification attempts
    """
    import time

    t0 = time.time()

    token = os.getenv("ANYSCALE_API_KEY", None)
    if not token:
        log.error("Missing ANYSCALE API token.")
        return None

    stats = await fn.get_current_stats.aio()
    max_running = 180
    # alternatively, we may want to fall back if our function has a queue: stats.backlog > 0
    if ENABLE_ANYSCALE_FALLBACK:
        compose_state = ModalDict.lookup("compose-state", environment_name="main")
        running_key = "running-mistral-7b-instruct"
        running = compose_state.get(running_key, 0)
        prompts = args.get("prompts")
        num_reqs = len(prompts)

        if running + num_reqs < max_running:
            dd = Function.lookup("datadog", "log_event")
            dd.spawn(
                message="ATTEMPT: mistral-7b fallback",
                name="mistral-7b-instruct-fallback",
                attributes={
                    "backlog": stats.backlog,
                    "active_runners": stats.num_active_runners,
                    "total_runners": stats.num_total_runners,
                },
            )
            kwargs = {k: v for k, v in args.items() if k != "prompts"}
            compose_state[running_key] = running + num_reqs
            _runs: List[InferenceRun[List[MistralResult], MistralUsage]] = await asyncio.gather(
                *[
                    _run_mistral_anyscale(
                        prompt=prompt,
                        **kwargs,
                        req=req,
                    )
                    for prompt in prompts
                ]
            )
            compose_state[running_key] = max(0, compose_state.get(running_key, 0) - num_reqs)

            failed_indexes = [i for i, r in enumerate(_runs) if not r]
            retry_prompts = [prompts[i] for i in failed_indexes]

            if failed_indexes:
                met = Function.lookup("datadog", "log_metric", environment_name="main")
                met.spawn(
                    name="anyscale-fallback-failures",
                    value=len(failed_indexes),
                )
                log.info(f"anyscale fallback failed, {len(failed_indexes)} of {len(prompts)} failed")
                retry_res: Union[InferenceRun[List[MistralResult], MistralUsage], None] = await fn.remote.aio(
                    prompts=retry_prompts, req=req, **kwargs
                )
                log.info(f"anyscale fallback-fallback, {len(retry_res.result)}")
            else:
                retry_res = None

            all_results = []
            failed_index = 0

            token_count = retry_res.usage.output_token_count if retry_res else 0
            input_token_count = retry_res.usage.input_token_count if retry_res else 0

            for _, r in enumerate(_runs):
                if r:
                    all_results.append(r.result[0])
                    token_count += r.usage.output_token_count
                    input_token_count += r.usage.input_token_count
                else:
                    all_results.append(retry_res.result[failed_index])
                    failed_index += 1

            if len(all_results) == len(prompts):
                log.info(f"collected results with fallback, {len(failed_indexes)} / {len(prompts)} failed")
                met = Function.lookup("datadog", "log_metric", environment_name="main")
                met.spawn(
                    name="anyscale-fallback-tokens",
                    value=token_count
                    + input_token_count
                    - (retry_res.usage.output_token_count if retry_res else 0)
                    - (retry_res.usage.input_token_count if retry_res else 0),
                )
                execution_s = time.time() - t0
                usage = MistralUsage(
                    execution_seconds=execution_s,
                    machine_config="Vendor",
                    output_token_count=token_count,
                    input_token_count=input_token_count,
                )
                return InferenceRun(result=all_results, usage=usage)
            else:
                log.info("failed to collect results with fallback")

    return None
