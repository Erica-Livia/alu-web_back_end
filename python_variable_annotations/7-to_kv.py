#!/usr/bin/env python3


def to_kv(k: str, v: [int, float]) -> tuple:
    """
    function to_kv
    parameters
        k: string
        v: an int or float
    returns a tuple
    """

    return (k, float(v ** 2))
