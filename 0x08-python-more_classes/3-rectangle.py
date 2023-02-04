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

    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
    
    print(str(my_rectangle))
    print(repr(my_rectangle))


    print("--")


    my_rectangle.width = 14
    my_rectangle.height = 6
    print(my_rectangle)
    print(repr(my_rectangle))
