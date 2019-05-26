#!/usr/bin/python3.7
import functools


def dynamic_caching(function):
    cache = {}
    @functools.wraps(function)
    def result(*args, clear_cache=False,
                ignore_cache=False, skip_cache=False, **kwargs):
        nonlocal cache
        function_call = (args, tuple(kwargs.items()))
        if clear_cache:
            cache = {}
        if not ignore_cache and function_call in cache:
            return cache[function_call]
        out = function(*args, **kwargs)
        if not skip_cache:
            cache[function_call] = out
        return out
    return result
