#!/usr/bin/python3

"""This contains the MyList class."""

class MyList(list):
    """A class that inherits from the list superclass."""
    def __init__(self):
        """Performs the object initialization."""
        super().__init__()

    def print_sorted(self):
        """Displays the sorted list."""
        print(sorted(self))
