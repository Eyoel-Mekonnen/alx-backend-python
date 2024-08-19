#!/usr/bin/env python3
"""Type/Var Annotaton."""
from typing import Mapping, Union, Any, Optional, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[Optional[T], None] = None) -> Union[Any, T]:
    """TypeVar."""
    if key in dct:
        return dct[key]
    else:
        return default
