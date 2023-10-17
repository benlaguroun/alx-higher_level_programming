#!/usr/bin/python3
"""Specifies a function for converting a string to JSON format."""
import json


def to_json_string(my_obj):
    """Generate the JSON representation of a string object."""
    return json.dumps(my_obj)
