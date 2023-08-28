#!/usr/bin/python3

def safe_print_integer(value):
   """ Print an integer using the "{:d}".format() method.

   Args:
    value (int): The integer to print.

   Returns:
    bool: True if the integer was printed successfully, False if a TypeError or ValueError occurred.
 """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
