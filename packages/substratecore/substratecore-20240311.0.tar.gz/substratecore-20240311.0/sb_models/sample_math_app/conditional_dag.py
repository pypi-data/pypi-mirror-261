import os
from enum import Enum
from typing import Dict

from ray import serve
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Operation(str, Enum):
    ADDITION = "ADD"
    MULTIPLICATION = "MUL"


class MathRouterInternalSpec(BaseModel):
    operation: Operation
    input: int


@serve.deployment(
    ray_actor_options={
        "num_cpus": 0.1,
    }
)
@serve.ingress(app)
class Router:
    def __init__(self, multiplier, adder):
        self.adder = adder.options(use_new_handle_api=True)
        self.multiplier = multiplier.options(use_new_handle_api=True)

    @app.post("/")
    async def route(self, request: MathRouterInternalSpec) -> str:
        if request.operation == Operation.ADDITION:
            amount = await self.adder.add.remote(request.input)
        elif request.operation == Operation.MULTIPLICATION:
            amount = await self.multiplier.multiply.remote(request.input)

        return f"{amount} pizzas please!"


@serve.deployment(
    user_config={
        "factor": 3,
    },
    ray_actor_options={
        "num_cpus": 0.1,
        "runtime_env": {
            "env_vars": {
                "override_factor": "-2",
            }
        },
    },
)
class Multiplier:
    def __init__(self, factor: int):
        self.factor = factor

    def reconfigure(self, config: Dict):
        self.factor = config.get("factor", -1)

    @app.post("/multiply")
    def multiply(self, input_factor: int) -> int:
        if os.getenv("override_factor") is not None:
            return input_factor * int(os.getenv("override_factor", "0"))
        return input_factor * self.factor


@serve.deployment(
    user_config={
        "increment": 2,
    },
    ray_actor_options={
        "num_cpus": 0.1,
        "runtime_env": {
            "env_vars": {
                "override_increment": "-2",
            }
        },
    },
)
class Adder:
    def __init__(self, increment: int):
        self.increment = increment

    def reconfigure(self, config: Dict):
        self.increment = config.get("increment", -1)

    @app.post("/add")
    def add(self, input: int) -> int:
        if os.getenv("override_increment") is not None:
            return input + int(os.getenv("override_increment", "0"))
        return input + self.increment


@serve.deployment(
    ray_actor_options={
        "num_cpus": 0.1,
    }
)
@app.post("/order")
def create_order(amount: int) -> str:
    return f"{amount} pizzas please!"


# Overwritten by user_config
ORIGINAL_INCREMENT = 1
ORIGINAL_FACTOR = 1

multiplier = Multiplier.bind(ORIGINAL_FACTOR)
adder = Adder.bind(ORIGINAL_INCREMENT)
serve_dag = Router.bind(multiplier, adder)
