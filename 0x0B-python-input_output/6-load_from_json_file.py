#!/usr/bin/python3
"""Specifies a function for reading data from a JSON file."""
import json


def load_from_json_file(filename):
    """Instantiate a Python object using data from a JSON file."""
    with open(filename) as f:
        return json.load(f)
