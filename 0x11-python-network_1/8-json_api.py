#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    response = requests.post(
        "http://0.0.0.0:5000/search_user", data={'q': letter})

    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("No result")
