#!/usr/bin/python3

"""Defines a Rectangle class."""

class Rectangle:
    """Representation of Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the width rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for priv instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter fot height priv inst"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError(" height must be >= 0")
        self.__height = value

    def area(self):
        """return the Area of rectanagle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        p = 2 * (self.__width + self.__height)
        return p

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_p = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle_p += "#"
            if i != self.height - 1:
                rectangle_p += "\n"

        return rectangle_p

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
