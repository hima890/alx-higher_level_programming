#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_characters = []
        for character in my_string:
            if character not in "Cc":
                new_characters.append(character)
        return ''.join(new_characters)
    else:
        return ""
