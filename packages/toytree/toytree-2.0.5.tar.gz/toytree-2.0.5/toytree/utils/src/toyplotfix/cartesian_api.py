#!/usr/bin/env python

"""Wrapper that allows wrapping a method to a class.

"""

from functools import wraps


def add_cartesian_method(cls):
    """Clever approach to copy docstring and signature from func to API.

    Reference
    ---------
    https://mgarod.medium.com/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6
    """
    def decorator(func):

        # creates a wrapper for a Cartesian.{function} that copies
        # its docstring and arg signatures but sets axes as the
        # first argument of the function.
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)

        # sets: TreeModAPI.{function} = wrapper
        # TODO: remove first arg from signature and docs.
        setattr(cls, func.__name__, wrapper)

        # Note we are not binding func, but wrapper which accepts self
        # but does exactly the same as func.
        # returning func means func can still be used normally
        return func
    return decorator


if __name__ == "__main__":

    from toytree.utils.src.toyplotfix.cartesian import Cartesian

    @add_cartesian_method(Cartesian)
    def test(axes: Cartesian, arg2: str) -> float:
        """This is a test."""
        return 32.0

    help(test)
    help(Cartesian.test)
