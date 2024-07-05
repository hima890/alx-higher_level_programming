#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""

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
