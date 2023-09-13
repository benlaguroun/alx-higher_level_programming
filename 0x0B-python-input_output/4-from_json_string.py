#!/usr/bin/python3
# 6-from_json_string.py
"""Specifies a function for converting JSON data into an object."""
import json


def from_json_string(my_str):
    """Produce the Python object representation of a JSON string."""
    return json.loads(my_str)
