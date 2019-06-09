#!/usr/bin/python3.7
from __future__ import annotations
""" Test the parser for interpreting Excel-like
    syntax. The program should either read the input
    and return the correct address, array of addresses,
    or even throw the correct errors."""
import re
import pandas as pd
import string
import functools

async def async_dynamic(coroutine):
    cache = {}
    @functools.wraps(coroutine)
    async def async_result(*args, clear_cache=False,
                      ignore_cache=False, skip_cache=False, **kw):
        nonlocal cache
        coroutine_call = (args, tuple(kw.items()))
        if clear_cache:
            cache = {}
        if not ignore_cache and coroutine_call in cache:
            return cache[coroutine_call]
        out = await coroutine(*args, **kwargs)
        if not skip_cache:
            cache[coroutine_call] = await out
        return await out
    return await result

async def babysteps():
    addr = 'a1'
    Addr = 'A2'
    aRange = 'a5:g6'
    badRange = 'B1:A3'
    hardRange = 'BD12:BE14'
    return addr, Addr, aRange \
            badRange, hardRange

@async_dynamic
async def core_frame():
    aioframe = []
    internal = {
            "input": '',
            "value": 0,
            "hide_input": True
        }
    
