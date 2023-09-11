#!/usr/bin/python3
"""defines MyList Class"""


class MyList(list):
    """prints list in ascending order"""

    def print_sorted(self):
        print(sorted(self))
