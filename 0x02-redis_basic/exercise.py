#!/usr/bin/env python3
"""Exercise for Redis"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator count number of calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator store the history of inputs and outputs"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        input = str(args)
        self._redis.rpush("{}:inputs".format(key), input)

        output = str(method(self, *args, **kwds))
        self._redis.rpush("{}:outputs".format(key), output)

        return output
    return wrapper

