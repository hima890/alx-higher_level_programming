#!/usr/bin/python3
import sys
argLen = len(sys.argv)
arguments = sys.argv
if argLen == 1:
    print("{} arguments.".format(argLen))
elif argLen == 2:
    print("1 argument:".format(argLen))
    print("1: {}".format(arguments[1]))
elif argLen > 2:
    print("{} arguments:".format(argLen - 1))
    for index in range(argLen):
        if index == 0:
            continue
        print("{}: {}".format(index, arguments[index]))
