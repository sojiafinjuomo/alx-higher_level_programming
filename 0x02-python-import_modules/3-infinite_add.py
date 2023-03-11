#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    sum_args = 0
    for i in range(count):
        sum_args = sum_args + int(sys.argv[i + 1])
    print(sum_args)
