#!/usr/bin/python3
"""Specifies a function for reading text files."""


def read_file(filename=""):
    """Display the contents of a UTF-8 text file on the standard output."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
