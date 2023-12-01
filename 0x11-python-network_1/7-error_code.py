#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""
from requests import get
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with get(url) as response:
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
