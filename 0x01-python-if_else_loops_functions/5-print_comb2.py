#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print(f"0{number}, ", end="")
    else:
        if number == 99:
            print(f"{number}")
        else:
            print(f"{number}, ", end="")