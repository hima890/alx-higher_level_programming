#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argLen = len(sys.argv)
    arguments = sys.argv
    if argLen < 4:
        print("Usage: .{} <a> <operator> <b>".format(arguments[0]))
        sys.exit(1)
    if argLen == 4:
        operators = ['+', '-', '*', '/']
        operator = arguments[2]
        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(arguments[1])
            b = int(arguments[3])
            if operator == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif operator == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif operator == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            elif operator == '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
