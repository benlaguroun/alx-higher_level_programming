#!/usr/bin/python3
"""Describes a function responsible for retrieving object attributes."""


def lookup(obj):
    """Generate a list of attributes accessible for a given object."""
    return (dir(obj))
