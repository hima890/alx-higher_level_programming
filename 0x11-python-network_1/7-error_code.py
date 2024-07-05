#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""

# Code should not be executed when imported
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    # Send the request to the URL
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        # Display the response body decoded in utf-8
        print(response.text)
