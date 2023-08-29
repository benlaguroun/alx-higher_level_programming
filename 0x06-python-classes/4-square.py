#!/usr/bin/python3
"""
This script defines a class Square representing a square shape.
"""
class Square:
    """
    This class represents a square shape and provides methods to work with it.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square's sides.
        """
        self.size = size  # Use the setter to set the size
    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
            value (int): The new size for the square.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be a non-negative integer.")
        self.__size = value
    def area(self):
        """
        Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
