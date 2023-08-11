#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    num_argv = len(sys.argv) - 1
    if num_argv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        0p = sys.argv[2]
        b = int(sys.argv[3])
        if op not in ('+', '-', '*', '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            result = int(a op b)
            print("{} {} {} = {}".format(a, op, b, result))
