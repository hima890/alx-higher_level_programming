#!/bin/bash
# A Bash script that sends a GET request to a URL and displays the body of the response
curl -sL --request GET "$1" --write-out "%{http_code}" --output /dev/null | grep -q "200" && curl -sL "$1"
