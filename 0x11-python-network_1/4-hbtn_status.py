#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
from requests import get


if __name__ == '__main__':
    with get("https://alx-intranet.hbtn.io/status") as response:
        print("Body response:")
        print(f"\t- type: {type(str(response))}")
        print(f"\t- content: {response.text}")
