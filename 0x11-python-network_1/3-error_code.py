#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

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
