#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
import redis
import time


# Create a Redis client
redis_client = redis.Redis()

def get_page(url: str) -> str:
    """Gets the HTML content of a particular URL and returns it"""
    # Check if the URL is already cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode()

    # Make the request to the URL
    response = requests.get(url)

    # Store the content in the cache with an expiration time of 10 seconds
    redis_client.setex(url, 10, response.text)

    # Track the number of times the URL is accessed
    redis_client.incr(f"count:{url}")

    return response.text
