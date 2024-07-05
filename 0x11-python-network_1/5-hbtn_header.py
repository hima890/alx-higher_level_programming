#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to
the URL and displays the value of the variable X-Request-Id
in the response header"""

# Code should not be executed when imported
if __name__ == "__main__":
    import requests
    import sys

    # Request the URL
    url = sys.argv[1]
    request = requests.get(url)
    # Read the response headers
    print("{}".format(request.headers.get("X-Request-Id")))
