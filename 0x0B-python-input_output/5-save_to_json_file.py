#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON."""
    with open(filename, "w") as w_f:
        json.dump(my_obj, w_f)
