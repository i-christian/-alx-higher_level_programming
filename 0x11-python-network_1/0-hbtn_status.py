#!/usr/bin/python3
from urllib.request import urlopen
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""


with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()


if __name__ == "__main__":
   print( body[:15])
