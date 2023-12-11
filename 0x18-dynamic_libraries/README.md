Dynamic Libraries Project
This project involves creating dynamic libraries, calling C functions from Python, and implementing code injection for a specific scenario. Below are details and instructions for each part of the project.

1. Dynamic Library (libdynamic.so)
The first task is to create a dynamic library called libdynamic.so containing various C functions. These functions include string manipulation, character checks, and basic arithmetic operations. The list of functions is specified in the main.h header file. The dynamic library is compiled from the provided source files.

Compilation and Usage
bash
Copy code
# Compile the dynamic library
gcc -Wall -Werror -pedantic -Wextra -fPIC -shared *.c -o libdynamic.so

# Test the library with a sample program
gcc -Wall -Werror -pedantic -Wextra -L. 0-main.c -ldynamic -o len
./len
2. Create Dynamic Library Script (1-create_dynamic_lib.sh)
The second task involves creating a script (1-create_dynamic_lib.sh) that automates the process of generating a dynamic library. The script compiles all C files in the current directory into a shared library named liball.so.

Usage
bash
Copy code
./1-create_dynamic_lib.sh
3. Call C Functions from Python (100-operations.so)
In this task, a dynamic library (100-operations.so) is created with C functions that can be called from Python. The Python script 100-tests.py demonstrates calling these C functions from Python.

Python Script Execution
bash
Copy code
python3 100-tests.py
4. Code Injection (101-make_me_win.sh)
The final task involves code injection to make the user win in a fictional lottery program (gm). The script 101-make_me_win.sh injects code using LD_PRELOAD to manipulate the lottery numbers before running the program.

Execution
bash
Copy code
. ./101-make_me_win.sh
This script creates a shared library (hijack.so) and sets LD_PRELOAD to load the library before executing the gm program, ensuring the desired numbers are used.

Note: This code is for educational purposes only and should not be used for any malicious activities.