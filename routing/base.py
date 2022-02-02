import typing as t
from starlette.routing import Router, Mount
from .operations import Operation, WebsocketOperation
from .route_definitions import RouteDefinitions

__all__ = ['ModuleRouter', 'APIRouter']


class ModuleRouter(Mount):
    def __init__(
            self,
            path: str,
            name: str = None,
    ) -> None:
        super(ModuleRouter, self).__init__(path=path, routes=[], name=name)
        self._route_definitions = RouteDefinitions(Operation, WebsocketOperation, self.app.routes)
        self._has_requested_routes = False

        self.Get = self._route_definitions.get
        self.Post = self._route_definitions.post

        self.Delete = self._route_definitions.delete
        self.Patch = self._route_definitions.patch

        self.Put = self._route_definitions.put
        self.Options = self._route_definitions.options

        self.Trace = self._route_definitions.trace
        self.Head = self._route_definitions.head

        self.Route = self._route_definitions.route
        self.Websocket = self._route_definitions.websocket


class APIRouter(Router):
    def __init__(self, *args: t.Any, **kwargs: t.Any):
        super().__init__(*args, **kwargs)

        self._route_definitions = RouteDefinitions(Operation, WebsocketOperation, self.routes)
        self._has_requested_routes = False

        self.Get = self._route_definitions.get
        self.Post = self._route_definitions.post

        self.Delete = self._route_definitions.delete
        self.Patch = self._route_definitions.patch

        self.Put = self._route_definitions.put
        self.Options = self._route_definitions.options

        self.Trace = self._route_definitions.trace
        self.Head = self._route_definitions.head

        self.Route = self._route_definitions.route
        self.Websocket = self._route_definitions.websocket

    def route(
            self,
            path: str,
            methods: t.List[str] = None,
            name: str = None,
            include_in_schema: bool = True,
    ) -> t.Callable:
        # TODO
        """Override with new configuration"""

    def websocket_route(self, path: str, name: str = None) -> t.Callable:
        # TODO
        """Override with new configuration"""

    def add_route(
            self,
            path: str,
            endpoint: t.Callable,
            methods: t.List[str] = None,
            name: str = None,
            include_in_schema: bool = True,
    ) -> None:
        # TODO
        """Override with new configuration"""

    def add_websocket_route(
            self, path: str, endpoint: t.Callable, name: str = None
    ) -> None:
        # TODO
        """Override with new configuration"""
