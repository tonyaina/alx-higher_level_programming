#!/usr/bin/python3
"""Define a class Rectangle."""

class Rectangle:
    """Represent a class rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            size (int): the size of the new rectangle."""

        self.width = width
        self.height = height

    @property

    def width(self):
        """Retrieve the current size of the rectangle."""
        return (self.__width)

    @width.setter

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property

    def height(self):
        """Retrieve the current size of the rectangle."""
        return (self.__height)

    @height.setter

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the current perimeter of the rectangle."""
        return (2*self.width + 2*self.height)
