#!/usr/bin/python3
for character in range(122, 96, -1):
    if character % 2 == 0:
        print(f"{chr(character)}", end="")
    else:
        print(f"{chr(character - 32)}", end="")