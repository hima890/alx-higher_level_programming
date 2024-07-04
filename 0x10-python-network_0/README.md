# alx-higher_level_programming: 0x10-python-network_0

This repository contains solutions to tasks related to HTTP requests using `curl`. Each script is designed to perform a specific function as described below:

## Tasks

### 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes. You have to use `curl`.

- **File**: `0-body_size.sh`

### 1. cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response. Display only the body of a 200 status code response. You have to use `curl`.

- **File**: `1-body.sh`

### 2. cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response. You have to use `curl`.

- **File**: `2-delete.sh`

### 3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept. You have to use `curl`.

- **File**: `3-methods.sh`

### 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`. You have to use `curl`.

- **File**: `4-header.sh`

### 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. Send a variable `email` with the value `test@gmail.com` and a variable `subject` with the value `I will always be here for PLD`. You have to use `curl`.

- **File**: `5-post_params.sh`

### 6. Find a peak
Write a function that finds a peak in a list of unsorted integers. The function should have the lowest complexity possible.

- **Files**: `6-peak.py`, `6-peak.txt`

### 7. Only status code
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response. You are not allowed to use any pipe, redirection, etc. You have to use `curl`.

- **File**: `100-status_code.sh`

### 8. cURL a JSON file
Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request. You have to use `curl`.

- **File**: `101-post_json.sh`

### 9. Catch me if you can!
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response. You have to use `curl`. You are not allowed to use `echo`, `cat`, etc. to display the final result.

- **File**: `102-catch_me.sh`

## Repository Structure
- **Directory**: `0x10-python-network_0`
- **Files**:
  - `0-body_size.sh`
  - `1-body.sh`
  - `2-delete.sh`
  - `3-methods.sh`
  - `4-header.sh`
  - `5-post_params.sh`
  - `6-peak.py`
  - `6-peak.txt`
  - `100-status_code.sh`
  - `101-post_json.sh`
  - `102-catch_me.sh`

Make sure to test your scripts in the provided sandbox environment using the web server running on port 5000.
