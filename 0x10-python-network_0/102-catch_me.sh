#!/bin/bash
# A Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
