# Python - Hello, World

This repository contains Python scripts and a C program as part of the ALX Software Engineering Program.

## Contents

### 0. Run Python file
A Shell script (`0-run`) that runs a Python script. The Python file name is saved in the environment variable `$PYFILE`.

```bash
$ cat main.py
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./0-run
Best School
```

### 1. Run inline
A Shell script (`1-run_inline`) that runs Python code. The Python code is saved in the environment variable `$PYCODE`.

```bash
$ export PYCODE='print(f"Best School: {88+10}")'
$ ./1-run_inline
Best School: 98
```

### 2. Hello, print
A Python script (`2-print.py`) that prints the string "Programming is like building a multilingual puzzle," followed by a new line.

```bash
$ ./2-print.py
Programming is like building a multilingual puzzle
```

### 3. Print integer
A Python script (`3-print_number.py`) that prints the integer stored in the variable `number`, followed by "Battery street," and a new line.

```bash
$ ./3-print_number.py
98 Battery street
```

### 4. Print float
A Python script (`4-print_float.py`) that prints the float stored in the variable `number` with a precision of 2 digits.

```bash
$ ./4-print_float.py
Float: 3.14
```

### 5. Print string
A Python script (`5-print_string.py`) that prints the string stored in the variable `str` three times, followed by its first 9 characters.

```bash
$ ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

### 6. Play with strings
A Python script (`6-concat.py`) that prints "Welcome to Holberton School!" without using any loops or conditional statements.

```bash
$ ./6-concat.py
Welcome to Holberton School!
```

### 7. Copy - Cut - Paste
A Python script (`7-edges.py`) that prints the first 3 letters, last 2 letters, and middle word of the variable `word`.

```bash
$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

### 8. Create a new sentence
A Python script (`8-concat_edges.py`) that prints "object-oriented programming with Python" without using any loops or conditional statements.

```bash
$ ./8-concat_edges.py
object-oriented programming with Python
```

### 9. Easter Egg
A Python script (`9-easter_egg.py`) that prints "The Zen of Python" by Tim Peters.

```bash
$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
Namespaces are one honking great idea -- let's do more of those!
```

### 10. Linked list cycle
A C program (`10-check_cycle.c`) that checks if a singly linked list has a cycle in it.

```bash
$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
$ ./cycle
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
```

### 11. Hello, write
A Python script (`100-write.py`) that prints "and that piece of art is useful - Dora Korpar, 2015-10-19" to stderr and exits with status code 1.

```bash
$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
$ echo $?
1
```

### 12. Compile
A Shell script (`101-compile`) that compiles a Python script file. The Python file name is stored in the environment variable `$PYFILE`.

```bash
$ cat main.py
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./101-compile
Compiling main.py ...
$ ls
101-compile  main.py  main.pyc
$ cat main.pyc | zgrep -c "Best School"
1
$ od -t x1 main.pyc # SYSTEM DEPENDENT => CAN BE DIFFERENT
...
```

### 13. ByteCode -> Python #1
A Python function (`102-magic_calculation.py`) that performs the same as given Python bytecode.

```python
def magic_calculation(a, b):
    # Equivalent to given Python bytecode
    # 3           0 LOAD_CONST               1 (98)
    #             3 LOAD_FAST                0 (a)
    #

             6 LOAD_FAST                1 (b)
    #             9 BINARY_POWER
    #            10 BINARY_ADD
    #            11 RETURN_VALUE
    return 98 + (a ** b)
```