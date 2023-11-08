#!/usr/bin/python3
"""Module that creates a square class"""


class Square:
    """Creates Square class"""

    def __init__(self, width=0, height=0):
        """init method that initialises attributes"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the square"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the square"""
        return 2 * (self.width + self.height)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
