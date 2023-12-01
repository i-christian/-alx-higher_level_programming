#!/usr/bin/python3
"""A Python script that sends a POST request with an email as a parameter"""

import sys
from requests import post

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    with post(url, data=data) as response:
        print(response.text)
