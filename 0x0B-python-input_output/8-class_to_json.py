#!/usr/bin/python3
"""Specifies a function for converting a Python class to its JSON representation."""


def class_to_json(obj):
    """Provide  the dictionary represntation of a simple data structure."""
    return obj.__dict__
