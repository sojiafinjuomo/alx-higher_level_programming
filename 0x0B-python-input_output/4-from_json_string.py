#!/usr/bin/python3
"""
A function that returns an object (Python data structure)
represented by a JSON string:
"""


def from_json_string(my_str):
    """calls the function and imports json"""
    import json
    return json.loads(my_str)
