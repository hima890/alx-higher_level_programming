#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print("0{}, ".format(number), end="")
    else:
        if number == 99:
            print("{}".format(number))
        else:
            print("{}, ".format(number), end="")
