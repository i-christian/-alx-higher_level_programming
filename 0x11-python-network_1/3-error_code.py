#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""
from  urllib.error import HTTPError
import sys
from urllib.request import urlopen

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            content = response.read().decode('utf-8')
            print (content)
    except HTTPError as err:
        print(f"Error code: {err.code}")
