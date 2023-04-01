#!/usr/bin/python3
"""A Python script that sends a POST request with an email as a parameter"""

import sys
from urllib.request import urlopen
from urllib.parse import urlencode

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({'email': email}).encode('utf-8')
    with urlopen(url, data) as response:
        content = response.read().decode('utf-8')
        print(content)
