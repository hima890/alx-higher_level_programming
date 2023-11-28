#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
string_1 = f"Last digit of {number} is -{lastDigit} and is greater than 5"
string_2 = f"Last digit of {number} is {abs(lastDigit)} and is greater than 5"
string_3 = f"Last digit of {number} is
-{lastDigit} and is less than 6 and not 0"
string_4 = f"Last digit of {number} is
{lastDigit} and is less than 6 and not 0"
if number > 5:
    if number < 0:
        print(string_1)
    else:
        print(string_2)
elif number == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
elif (number < 6) and (number != 0):
    if number < 0:
        print(string_3)
    else:
        print(string_4)
