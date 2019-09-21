from inspect import signature
from functools import partial


def curry(fn):
    def inner(arg):
        if len(signature(fn).parameters) == 1:
            return fn(arg)
        return curry(partial(fn, arg))
    return inner


# @curry
class add(int):
    def __call__(self, value):
        return add(self + value)
