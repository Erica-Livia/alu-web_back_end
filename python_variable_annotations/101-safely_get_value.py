#!/usr/bin/env python3


"""
adding type anotation to the function
"""


from typing import TypeVar, Mapping, Any, Union


K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Mapping[K, V], key: Any, default: Union[V, None] = None) -> Union[V, None]:
    """
    Safely retrieves a value from a dictionary.

    Parameters:
        dct (Mapping[K, V]): The input dictionary.
        key (K): The key to retrieve the value for.
        default (Union[V, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[V, None]: The value associated with the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
