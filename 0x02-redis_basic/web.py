#!/usr/bin/env python3
""" Main file """

import requests
import redis
import time


def get_page(url: str) -> str:
    """
    uses the requests module to obtain the HTML
    content of a particular URL and returns it.

    Args:
        url (str): _description_

    Returns:
        str: content
    """
    # Initialize Redis client
    redis_client = redis.Redis()

    # Increment URL access count
    url_key = f"count:{url}"
    redis_client.incr(url_key)

    # Check if content is cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode("utf-8")

    # Make HTTP request to the URL
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    # Cache the HTML content with expiration
    if end_time - start_time <= 10:
        redis_client.setex(url, 10, response.content)

    return response.content.decode("utf-8")
