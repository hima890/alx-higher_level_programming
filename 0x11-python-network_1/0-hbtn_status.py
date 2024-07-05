#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

# Code should not be executed when imported
if __name__ == "__main__":
    import urllib.request

    # Request the URL
    url = 'https://alx-intranet.hbtn.io/status'
    request = urllib.request.Request(url)
    # Read the response countent
    with urllib.request.urlopen(request) as response:
        body = response.read()
        # Output the response body
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
