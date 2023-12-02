#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    arguments = sys.argv
    sum = 0
    for index in range(1, argLen):
        sum = sum + int(arguments[index])
    print("{}".format(sum))
