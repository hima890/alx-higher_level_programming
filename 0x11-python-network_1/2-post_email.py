#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response."""

# Code should not be executed when imported
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data for the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request
    with urllib.request.urlopen(url, data) as response:
        body = response.read()

    # Display the response body decoded in utf-8
    print(body.decode('utf-8'))
