#!/usr/bin/python3
"""Specifies a function for checking class types."""


def is_same_class(obj, a_class):
    """Determine if an object is an exact instance of a specified class.

    Args:
    obj (any): The object to check.
    a_class (type): The class to compare the type of obj to.

    Returns:
    True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
