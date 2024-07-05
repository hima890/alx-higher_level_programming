#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8)."""

# Code should not be executed when imported
if __name__ == "__main__":
    import urllib.request
    import sys

    # Request the URL
    url = sys.argv[1]
    request = urllib.request.Request(url)
    # Read the response countent
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("{}".format(body.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.reason))
