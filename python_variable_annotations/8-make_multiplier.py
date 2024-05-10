#!/usr/bin/env python3


def make_multiplier(multiplier: float):
    """
    function make_multiplier
    parameters
        multiplier: float
    returns a function that muliplies a float by multiplier
    """

    def multiplication(x: float) -> float:
        return (x * multiplier)

    return multiplication
