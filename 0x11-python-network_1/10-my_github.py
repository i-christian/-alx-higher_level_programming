#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_id = response.json()['id']
        print(user_id)
    else:
        print("None")
