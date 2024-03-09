import logging
import traceback
from dataclasses import dataclass
from typing import Any, Literal, Optional

from strawberry.extensions import SchemaExtension
from strawberry.types import Info

from nestipy.common.decorator import Module
from nestipy.core.module import NestipyModule
from nestipy.core.module.middleware import MiddlewareConsumer
from nestipy.plugins.dynamic_module.dynamic_module import DynamicModule
from nestipy.plugins.strawberry_module.compiler import GraphqlCompiler
from nestipy.plugins.strawberry_module.constant import STRAWBERRY_MODULE_OPTION
from nestipy.plugins.strawberry_module.strawberry_middleware import StrawberryMiddleware, ExecutionContextExtension


@dataclass
class StrawberryOption:
    graphql_ide: Optional[Literal["graphiql", "apollo-sandbox", "pathfinder"]]


@Module(providers=[])
class StrawberryModule(DynamicModule, NestipyModule):
    resolvers = []

    @classmethod
    def for_root(cls, option: Any = StrawberryOption(graphql_ide='graphiql'), imports=None):
        if imports is None:
            imports = []
        setattr(cls, 'resolvers', list(set(imports)))
        return cls.register(provide=STRAWBERRY_MODULE_OPTION, value=option)

    def configure(self, consumer: MiddlewareConsumer):
        if len(self.resolvers) > 0:
            try:
                gql_compiler = GraphqlCompiler(modules=self.resolvers)
                schema = gql_compiler.compile(extensions=[ExecutionContextExtension])
                setattr(StrawberryMiddleware, 'schema', schema)
                consumer.apply_for_route(self, '/graphql', StrawberryMiddleware)
            except Exception as e:
                tb = traceback.format_exc()
                logging.error(e)
                logging.error(tb)

    async def on_startup(self):
        pass
