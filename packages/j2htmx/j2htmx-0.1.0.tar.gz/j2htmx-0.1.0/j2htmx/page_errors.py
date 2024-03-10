class GenericRenderingError(BaseException):
    ...


class NotAllParamsSubstitutedError(GenericRenderingError):
    def __init__(self, var, component, params, file):
        self._var = var
        self._component = component
        self._params = params
        self._file = file

    def __str__(self):
        return (f'<h3>Template Substitution Error:</h1>'
                f'Variable: "{self._var}" not substituted for "{self._component}" ("'
                f'{self._file}") component by: {self._params}')


class ComponentNameNotSet(GenericRenderingError):
    def __init__(self, component, file):
        self._component = component
        self._file = file

    def __str__(self):
        return (f'<h3>Template Substitution Error:</h1>'
                f'Template {self._file} doesn\'t have "component" for "{self._component}"')
