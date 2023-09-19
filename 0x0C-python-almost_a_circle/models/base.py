#!/usr/bin/python3
"""Module for base class."""

class Base:
    """A representation of the base of our loop hiierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
