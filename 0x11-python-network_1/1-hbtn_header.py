#!/usr/bin/python3
"""a Python script that displays the value of the X-Request-Id variable"""

from urllib.request import urlopen
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urlopen(url) as response:
        request_id = response.info().get('X-Request-Id')
    # Print the ID
    print(request_id)
