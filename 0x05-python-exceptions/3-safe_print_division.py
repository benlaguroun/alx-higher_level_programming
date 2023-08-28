#!/usr/bin/python3

def safe_print_division(a, b):
"""
Calculate the result of dividing 'a' by 'b'.

Parameters:
    a (float or int): The dividend.
    b (float or int): The divisor.

Returns:
    float or None: The result of 'a' divided by 'b', or None if 'b' is 0.
"""
   try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
\
