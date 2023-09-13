#!/usr/bin/python3
"""Specifies a function for writing data to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Serialize an object and write it to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
