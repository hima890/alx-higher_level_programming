#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = ""
        for charchter in my_string:
            if charchter not in "Cc":
                new_string += charchter
            else:
                continue
        return (new_string)
    else:
        return (None)