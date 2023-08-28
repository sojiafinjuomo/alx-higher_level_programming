#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
<<<<<<< HEAD
    except(TypeError, ValueError):
=======
    except (TypeError, ValueError):
>>>>>>> 0d47fb35f061afd8e9e4ab5c8871b6980488bc75
        return (False)
