#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""
from requests.exceptions import HTTPError
from requests import get
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with get(url) as response:
            print(response.text)
    except HTTPError as err:
        code = err.response.status_code
        if code >= 400:
            print(f"Error code: {err.code}")
