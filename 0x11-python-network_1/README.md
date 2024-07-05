# 0x11. Python - Network #1

## Description
This project contains a series of Python scripts to demonstrate basic usage of the `urllib` and `requests` packages for making HTTP requests and handling responses. Each task focuses on specific aspects of making HTTP requests, handling response headers, sending POST requests, managing errors, and using the GitHub API.

## Requirements
- Python 3.x
- The `requests` package for tasks using the `requests` library.
- The `urllib` and `sys` packages for tasks using the `urllib` library.
- Internet connection for making HTTP requests.

## Tasks

### 0. What's my status? #0
Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using the `urllib` package. The body of the response must be displayed like the following example (tabulation before `-`):
```bash
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$
```
- You must use the package `urllib`.
- You are not allowed to import any packages other than `urllib`.
- You must use a `with` statement.

**File:** `0-hbtn_status.py`

### 1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

```bash
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$
```
- You must use the packages `urllib` and `sys`.
- You are not allowed to import packages other than `urllib` and `sys`.
- The value of this variable is different for each request.
- You don’t need to check arguments passed to the script (number or type).
- You must use a `with` statement.

**File:** `1-hbtn_header.py`

### 2. POST an email #0
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8).

```bash
guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$
```
- The email must be sent in the `email` variable.
- You must use the packages `urllib` and `sys`.
- You are not allowed to import packages other than `urllib` and `sys`.
- You don’t need to check arguments passed to the script (number or type).
- You must use a `with` statement.

**File:** `2-post_email.py`

### 3. Error code #0
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

```bash
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$
```
- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the HTTP status code.
- You must use the packages `urllib` and `sys`.
- You are not allowed to import packages other than `urllib` and `sys`.
- You don’t need to check arguments passed to the script (number or type).
- You must use a `with` statement.

**File:** `3-error_code.py`

### 4. What's my status? #1
Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using the `requests` package. The body of the response must be displayed like the following example (tabulation before `-`):

```bash
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$
```
- You must use the package `requests`.
- You are not allowed to import packages other than `requests`.

**File:** `4-hbtn_status.py`

### 5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header.

```bash
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/0x11$
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
guillaume@ubuntu:~/0x11$
```
- You must use the packages `requests` and `sys`.
- You are not allowed to import other packages than `requests` and `sys`.
- The value of this variable is different for each request.
- You don’t need to check script arguments (number and type).

**File:** `5-hbtn_header.py`

### 6. POST an email #1
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

```bash
guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$
```
- The email must be sent in the variable `email`.
- You must use the packages `requests` and `sys`.
- You are not allowed to import packages other than `requests` and `sys`.
- You don’t need to error check arguments passed to the script (number or type).

**File:** `6-post_email.py`

### 7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

```bash
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$
```
- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code.
- You must use the packages `requests` and `sys`.
- You are not allowed to import packages other than `requests` and `sys`.
- You don’t need to check arguments passed to the script (number or type).

**File:** `7-error_code.py`

### 8. Search API
Write a Python script that takes in a letter and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

```bash
guillaume@ubuntu:~/0x11$ ./8-json_api.py
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
guillaume@ubuntu:~/0x11$
```
- The letter must be sent in the variable `q`.
- If no argument

 is given, set `q=""`.
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`.
- Otherwise:
  - Display `Not a valid JSON` if the JSON is invalid.
  - Display `No result` if the JSON is empty.
- You must use the package `requests` and `sys`.
- You are not allowed to import packages other than `requests` and `sys`.

**File:** `8-json_api.py`

### 9. My GitHub!
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.

```bash
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
guillaume@ubuntu:~/0x11$
```
- You must use Basic Authentication with a personal access token as password to access your information (only `read:user` permission is needed).
- The first argument will be your username.
- The second argument will be your password (in your case, a personal access token as password).
- You must use the package `requests` and `sys`.
- You are not allowed to import packages other than `requests` and `sys`.
- You don’t need to check arguments passed to the script (number or type).

**File:** `10-my_github.py`

### 10. Time for an interview!
Write a Python script that lists 10 commits (from the most recent to oldest) of the repository `rails` by the user `rails` using the GitHub API.

```bash
guillaume@ubuntu:~/0x11$ ./100-github_commits.py rails rails
3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França
f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França
0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França
8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França
guillaume@ubuntu:~/0x11$
```
- The first argument will be the repository name.
- The second argument will be the owner name.
- You must use the packages `requests` and `sys`.
- You are not allowed to import packages other than `requests` and `sys`.
- You don’t need to check arguments passed to the script (number or type).

**File:** `100-github_commits.py`

## Repository Structure
```
.
├── 0-hbtn_status.py
├── 1-hbtn_header.py
├── 2-post_email.py
├── 3-error_code.py
├── 4-hbtn_status.py
├── 5-hbtn_header.py
├── 6-post_email.py
├── 7-error_code.py
├── 8-json_api.py
├── 10-my_github.py
└── 100-github_commits.py
└── notes.txt
```

## Author
[Ibrahim Hanafi]