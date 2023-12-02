#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    arguments = sys.argv
    if argLen == 1:
        print("0 arguments.")
    elif argLen == 2:
        print("1 argument:".format(argLen))
        print("1: {}".format(arguments[1]))
    elif argLen > 2:
        print("{} arguments:".format(argLen - 1))
        for index in range(argLen):
            if index == 0:
                continue
            print("{}: {}".format(index, arguments[index]))
