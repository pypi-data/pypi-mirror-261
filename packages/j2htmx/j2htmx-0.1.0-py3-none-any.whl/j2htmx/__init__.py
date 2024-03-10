from .page_errors import GenericRenderingError, NotAllParamsSubstitutedError, ComponentNameNotSet
from .page import Component, InlineComponent
from .version import get_version

__version__ = get_version()
__all__ = (
    'GenericRenderingError', 'NotAllParamsSubstitutedError', 'ComponentNameNotSet'
    'Component', 'InlineComponent'
)
