#!/usr/bin/env python3
"""Exercise for Redis"""
import redis
import uuid


class Cache:
    """Cache class"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()