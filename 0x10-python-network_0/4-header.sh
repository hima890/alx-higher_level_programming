#!/bin/bash
# A Bash script that sends a GET request to a URL with a custom header and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
