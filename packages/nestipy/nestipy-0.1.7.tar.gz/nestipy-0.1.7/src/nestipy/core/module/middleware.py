from dataclasses import dataclass
from typing import Callable
from uuid import uuid4


@dataclass
class MiddlewareDict:
    middleware: Callable
    path: str = '/'
    guard: bool = False
    key: str = None


class MiddlewareConsumer:

    def __init__(self, compiler):
        self.compiler = compiler

    def apply_for_route(self, module, path, middleware):
        self.compiler.apply_middleware_to_path(module, path, [middleware])

    def apply_for_controller(self, module, ctrl, middleware):
        self.compiler.apply_middleware_to_ctrl(module, ctrl, [middleware])
