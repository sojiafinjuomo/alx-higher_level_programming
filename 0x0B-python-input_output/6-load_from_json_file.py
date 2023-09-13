#!/usr/bin/python3
"""
A function that creates an Object from a JSON file:
"""


def load_from_json_file(filename):
    """function that loads from json file"""
    import json
    with open(filename, "r", encoding="UTF8") as load_json:
        return json.load(load_json)
