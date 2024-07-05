#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""

# Code should not be executed when imported
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data for the POST request
    payload = {'email': email}

    # Send the POST request
    response = requests.post(url, data=payload)

    # Display the response body decoded in utf-8
    print(response.text)
