#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_argvs = len(sys.argv)-1
    if num_argvs == 0:
        print("{} arguments.".format(num_argvs))
    elif num_argvs == 1:
        print("{} argument: ".format(num_argvs))
    else:
        print("{} arguments: ".format(num_argvs))

    if num_argvs >= 1:
        num_argvs = 0
        for arg in sys.argv:
            if num_argvs != 0:
                print("{}: {}".format(num_argvs, arg))
            num_argvs += 1
