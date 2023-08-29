#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Print an integer using the "{:d}".format() method and handle ValueErrors

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

