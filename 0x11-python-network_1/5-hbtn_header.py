#!/usr/bin/python3
"""a Python script that displays the value of the X-Request-Id variable"""


from requests import get
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with get(url) as response:
        request_id = response.headers['X-Request-Id']
    # Print the ID
    print(request_id)
