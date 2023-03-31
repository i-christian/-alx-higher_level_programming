#!/usr/bin/python3
"""a Python script that displays the value of the X-Request-Id variable"""
from urllib.request import urlopen
import sys

url = sys.argv[1]
with urlopen(url) as response:
    request_id = response.info().get('X-Request-Id')

if __name__ == '__main__':
    print(request_id)
