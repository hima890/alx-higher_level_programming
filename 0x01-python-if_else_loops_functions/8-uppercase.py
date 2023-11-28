#!/usr/bin/python3
def uppercase(input_str):
    result_str = ""
    for char in input_str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert to uppercase using ASCII values
            result_str += chr(ord(char) - 32)
        else:
            result_str += char
    print("{}".format(result_str))
