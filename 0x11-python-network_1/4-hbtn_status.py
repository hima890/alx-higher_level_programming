#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
# Code should not be executed when imported
if __name__ == "__main__":
    import requests

    # Request the URL
    url = 'https://alx-intranet.hbtn.io/status'
    request = requests.get(url)

    # Read the response content
    body = request.text
    # Output the response body
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
