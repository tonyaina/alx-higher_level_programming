#!/usr/bin/python3
"""Define a class rectangle."""

class Rectangle:
    """Represent a class Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            size (int): The size of a new rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the current size of the rectangle."""
        return (sel.__width)

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
        return (self.width * self.height)

    def perimeter(self):
        return 2*(self.width + self.heigght)

    def my_print(self):
        """Print the rectangle with a # character."""
        for i in range(0, self.__width):
            for j in range(self.__height):
                print("#", end="")
                print("")
        
        if self.__width == 0:

            print("")

        if self.__height == 0:

            print("")

    def __str__(self):
        """prints a rectangle using '#'"""
        return f"{self.my_print()}"
