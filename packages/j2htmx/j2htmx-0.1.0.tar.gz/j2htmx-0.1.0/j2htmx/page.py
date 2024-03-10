import os
import re
import sys
from pathlib import Path
from typing import NamedTuple

import jinja2
from jinja2 import FileSystemLoader
from jinja2.meta import find_undeclared_variables

from .page_errors import ComponentNameNotSet
from .page_errors import GenericRenderingError
from .page_errors import NotAllParamsSubstitutedError

Params = NamedTuple


class Component:
    template_file: str = 'i.html'
    params = Params('EmptyParams')

    async def _get_component_file_path(self) -> Path:
        return Path(os.path.abspath(sys.modules[self.__module__].__file__))

    async def _get_component_path(self) -> Path:
        return Path(os.path.dirname(await self._get_component_file_path()))

    async def _get_component_template_file_path(self) -> Path:
        return await self._get_component_path() / self.template_file

    async def name(self):
        return await self._get_component_dir_name()

    async def _get_component_dir_name(self) -> str:
        return os.path.basename(await self._get_component_path())

    def __init__(self, params=None, check_template_for_component=True, **kwargs):
        if params is None:
            params = {}
        self.params = params | kwargs
        self.check_template_for_component = check_template_for_component

    async def _check_file_all_substituted(self, kwargs):
        component_path = await self._get_component_path()
        component_template_path = await self._get_component_template_file_path()

        with open(component_template_path) as file:
            environment = jinja2.Environment(loader=FileSystemLoader(component_path))
            template_ast = environment.parse(file.read())

        template_vars = find_undeclared_variables(template_ast)
        for var in template_vars:
            if var not in kwargs:
                raise NotAllParamsSubstitutedError(var, await self.name(), kwargs,
                                                   component_template_path)

        if self.check_template_for_component and 'component' not in template_vars:
            raise ComponentNameNotSet(await self.name(), component_template_path)

        return None

    async def render_subs_params(self):
        params = {'component': await self.name()}
        for key, value in self.params.items():
            if isinstance(value, list):
                params[key] = []
                for item in value:
                    if isinstance(item, Component):
                        params[key].append(a := await item._render())
                        continue
                    params[key].append(item)
                continue

            if isinstance(value, Component):
                params[key] = await value._render()
                continue

            params[key] = value
        return params

    async def _render(self, **kwargs):
        params = await self.render_subs_params()

        await self._check_file_all_substituted(params | kwargs)

        environment = jinja2.Environment(
            loader=FileSystemLoader(await self._get_component_path())
        )
        template = environment.get_template(self.template_file)
        return template.render(**params, **kwargs, component_name=await self.name())

    async def finalize(self, **kwargs):
        try:
            return await self._render(**kwargs)
        except GenericRenderingError as err:
            return str(err)

    async def selector(self):
        return f"#{await self.name()}"


class InlineComponent(Component):
    text = None

    async def _check_inline_all_substituted(self, kwargs):
        component_name = await self._get_component_dir_name()
        component_path = await self._get_component_path()
        component_template_path = await self._get_component_template_file_path()
        file = await self._get_component_file_path()

        environment = jinja2.Environment(loader=FileSystemLoader(component_path))
        html = re.sub(r"<!--(.|\s|\n)*?-->", "", self.text)
        template_ast = environment.parse(html)

        template_vars = find_undeclared_variables(template_ast)
        for var in template_vars:
            if var not in kwargs:
                raise NotAllParamsSubstitutedError(var, component_name, kwargs, file)

        if self.check_template_for_component and 'component' not in template_vars:
            raise ComponentNameNotSet(component_name, component_template_path)

        return None

    async def _render(self, **kwargs):
        params = await self.render_subs_params()

        await self._check_inline_all_substituted(params | kwargs)

        environment = jinja2.Environment()
        template = environment.from_string(self.text)
        return template.render(**params, **kwargs, component_name=await self.name())
