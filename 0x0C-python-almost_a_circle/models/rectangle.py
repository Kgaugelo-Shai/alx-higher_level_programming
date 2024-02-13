#!/usr/bin/python3
"""This defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This initializes a new Rectangle object

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x-coordinate of the rectangle in space
            y (int): The y-coordinate of the rectangle in space
            id (int): The unique id number of the new rectangle

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y coordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of rectangle"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for v in range(self.y)]
        for h in range(self.height):
            [print(" ", end='') for h in range(self.x)]
            [print('#', end='') for w in range(self.width)]
            print()

    def update(self, *args, **kwargs):
        """Updates a rectangle by updating each attribute
        Args:
            *args (int): new value to assign
                - 1st argument should be the id attribute
                - 2nd argument should be the width attribute
                - 3rd argument should be the height attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute
        """
        if args and len(args) != 0:
            c = 0
            for a in args:
                if c == 0:
                    if a is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = a
                elif c == 1:
                    self.width = a
                elif c == 2:
                    self.height = a
                elif c == 3:
                    self.x = a
                elif c == 4:
                    self.y = a
                c += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Returns information on the rectangle class"""
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        return string.format(self.id, self.x, self.y, self.width, self.height)
