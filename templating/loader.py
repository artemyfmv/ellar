import typing as t

from jinja2 import TemplateNotFound
from jinja2.loaders import BaseLoader
from .environment import Environment

if t.TYPE_CHECKING:
    from starletteapi.main import StarletteApp


class StarletteJinjaLoader(BaseLoader):
    """A loader that looks for templates in the application and all
    the blueprint folders.
    An idea from flask
    """

    def __init__(self, app: "StarletteApp") -> None:
        self.app = app

    def get_source(  # type: ignore
        self, environment: Environment, template: str
    ) -> t.Tuple[str, t.Optional[str], t.Optional[t.Callable]]:
        return self._get_source_fast(environment, template)

    def _get_source_fast(
        self, environment: Environment, template: str
    ) -> t.Tuple[str, t.Optional[str], t.Optional[t.Callable]]:
        for loader in self._iter_loaders(template):
            try:
                return loader.get_source(environment, template)
            except TemplateNotFound:
                continue
        raise TemplateNotFound(template)

    def _iter_loaders(self, template: str) -> t.Generator[BaseLoader, None, None]:
        loader = self.app.jinja_loader
        if loader is not None:
            yield loader

        for blueprint in self.app.get_module_loaders():
            loader = blueprint.jinja_loader
            if loader is not None:
                yield loader

    def list_templates(self) -> t.List[str]:
        result = set()
        loader = self.app.jinja_loader
        if loader is not None:
            result.update(loader.list_templates())

        for module_loader in self.app.get_module_loaders():
            loader = module_loader.jinja_loader
            if loader is not None:
                for template in loader.list_templates():
                    result.add(template)

        return list(result)
