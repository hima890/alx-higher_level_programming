#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

# Code should not be executed when imported
if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}

    try:
        # Send the POST request with the letter as a parameter
        response = requests.post(url, data=payload)

        # Raise an error for bad status codes
        response.raise_for_status()

        # Try to parse the response as JSON
        try:
            json_response = response.json()

            if json_response:
                # If the JSON response is not empty, display id and name
                print(
                    f"[{json_response.get('id')}] {json_response.get('name')}"
                    )
            else:
                # If the JSON response is empty
                print("No result")

        except ValueError:
            # If the response body is not properly JSON formatted
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"Request error occurred: {e}")
