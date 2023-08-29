#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Execute a function with error handling.

    Args:
        fct (callable): The function to execute.
        args: Arguments to pass to the function.

    Returns:
        Any: The result of the function call if successful, or None if an error occurs during execution.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)

