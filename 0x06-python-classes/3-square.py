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
        if not isinstance(size, int):
            raise TypeError("Size must be an integer.")
        elif size < 0:
            raise ValueError("size must be >= 0.")
        self.__size = size
    def area(self):
        """
        Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
