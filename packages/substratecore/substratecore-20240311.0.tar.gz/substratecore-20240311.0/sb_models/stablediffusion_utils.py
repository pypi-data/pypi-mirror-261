import random
from typing import List, Optional


def get_seed_generator(seed: Optional[int]) -> "torch.Generator":
    import torch

    if seed is None:
        return torch.Generator().manual_seed(random.getrandbits(64))
    else:
        return torch.Generator().manual_seed(seed)


def get_seed_generators(seeds: Optional[List[int]], num_images: int) -> List["torch.Generator"]:
    import torch

    if seeds is None:
        return [torch.Generator().manual_seed(random.getrandbits(64)) for _ in range(num_images)]
    else:
        if len(seeds) != num_images:
            raise ValueError(f"Number of seeds ({len(seeds)}) does not num_images" f" ({num_images})")
        return [torch.Generator().manual_seed(s) for s in seeds]


def set_scheduler(model, scheduler: str):
    """
    used in sd1.5 models, which we may not release
    """
    from diffusers import (
        DDIMScheduler,
        HeunDiscreteScheduler,
        DEISMultistepScheduler,
        EulerDiscreteScheduler,
        UniPCMultistepScheduler,
        DPMSolverMultistepScheduler,
        EulerAncestralDiscreteScheduler,
    )

    SCHEDULER_MAP = {
        "DPM++ Karras SDE": lambda config: DPMSolverMultistepScheduler.from_config(
            config, use_karras=True, algorithm_type="sde-dpmsolver++"
        ),
        "DPM++ Karras": lambda config: DPMSolverMultistepScheduler.from_config(config, use_karras=True),
        "Heun": lambda config: HeunDiscreteScheduler.from_config(config),
        "Euler a": lambda config: EulerAncestralDiscreteScheduler.from_config(config),
        "Euler": lambda config: EulerDiscreteScheduler.from_config(config),
        "DDIM": lambda config: DDIMScheduler.from_config(config),
        "DEIS": lambda config: DEISMultistepScheduler.from_config(config),
        "UniPCMultistep": lambda config: UniPCMultistepScheduler.from_config(config),
    }
    SCHEDULER_MAP["DPM++ 2M Karras"] = SCHEDULER_MAP["DPM++ Karras"]

    scheduler_fn = SCHEDULER_MAP.get(scheduler, None)

    if not scheduler_fn:
        raise ValueError(f"Sampler {scheduler} not found. Valid options are:" f" {list(SCHEDULER_MAP.keys())}")

    model.scheduler = scheduler_fn(model.scheduler.config)
    return scheduler_fn
