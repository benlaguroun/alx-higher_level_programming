#!/usr/bin/python3
"""
This script defines a class Square representing a square shape.
"""
class Square:
    """
    This class represents a square shape and provides methods to work with it.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square's sides.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position
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
    @property
    def position(self):
        """
        Get the position of the square.
        Returns:
            tuple: The position of the square.
        """
        return self.__position
    @position.setter
    def position(self, value):
        """
        Set the position of the square.
        Args:
            value (tuple): The new position for the square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of 2 positive integers.")
        self.__position = value
    def area(self):
        """
        Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
