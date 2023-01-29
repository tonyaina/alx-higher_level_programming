#!/usr/bin/python3
"""print Define a class Square."""

class Square:
    
    def __init__(size, size=0):
        """Initialize a new square.
        Args:
            size (int): the size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return (self.__size * self.__size)
