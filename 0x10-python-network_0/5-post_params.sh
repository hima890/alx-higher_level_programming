#!/bin/bash
# A Bash script that sends a POST request to a URL with specified data and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
