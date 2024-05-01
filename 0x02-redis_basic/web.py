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
    redis_client = redis.Redis()

    # Increment URL access count
    url_key = f"count:{url}"
    redis_client.incr(url_key)

    # Check if content is cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode("utf-8")

    # Make HTTP request to the URL
    response = requests.get(url)

    # Cache the HTML content with expiration
    redis_client.setex(url, 10, response.content)

    return response.content.decode("utf-8")


# Example usage
if __name__ == "__main__":
    # Test the function with a URL
    url = "http://slowwly.robertomurray.co.uk/\
        delay/5000/url/http://www.example.com"
    html_content = get_page(url)
    print(html_content)
