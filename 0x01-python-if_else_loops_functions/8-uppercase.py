#!/usr/bin/python3
def uppercase(input_str):
    for lowercase_char in input_str:
        if ord(lowercase_char) in range(97, 123):  # Check if the character is lowercase
            new_char = chr(ord(lowercase_char) - 32)  # Convert to uppercase
            print(new_char, end="")
        else:
            print(lowercase_char, end="")
    print("")
