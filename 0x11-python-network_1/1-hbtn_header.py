#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response."""

# Code should not be executed when imported
if __name__ == "__main__":
    import urllib.request
    import sys

    # Request the URL
    url = sys.argv[1]
    request = urllib.request.Request(url)
    # Read the response headers
    with urllib.request.urlopen(request) as response:
        headers = dict(response.getheaders())
        # Output the response body
        print("{}".format(headers.get("X-Request-Id")))
