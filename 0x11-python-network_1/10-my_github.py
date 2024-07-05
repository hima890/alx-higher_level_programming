#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL to get the authenticated user's information
    url = "https://api.github.com/user"

    # Use Basic Authentication with the provided username and token
    response = requests.get(url, auth=(username, token))

    # Check for HTTP errors
    if response.status_code == 200:
        try:
            # Parse the JSON response
            json_response = response.json()
            # Display the user id
            print(json_response.get('id'))
        except ValueError:
            print("Not a valid JSON")
    else:
        print("None")
