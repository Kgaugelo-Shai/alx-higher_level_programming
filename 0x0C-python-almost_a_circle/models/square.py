#!/usr/bin/python3
"""This defines a square class that inherits from
   a rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This initializes a square class

        Args:
            size (int): the dimensions of the square
            x (int): x coordinate of the square
            y (int): y cooordinate of the square
            id (int): The unique id of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.width = value

    def update(self, *args, **kwargs):
        """Updates the dimensions of the square object.

        Args:
            *args (ints): New attribute values.
                - 1st argument should be id attribute
                - 2nd argument should be  size attribute
                - 3rd argument should be x attribute
                - 4th argument should be y attribute
            **kwargs (dict): New key/value pairs of attribute to the instance.
        """
        if args and len(args) != 0:
            c = 0
            for a in args:
                if c == 0:
                    if c is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = a
                elif c == 1:
                    self.size = a
                elif c == 2:
                    self.x = a
                elif c == 3:
                    self.y = a
                c += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def area(self):
        """Returns the area of a square"""
        return (self.width * self.width)
    def to_dictionary(self):
        """Returns a dictionary representation of the square"""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Returns a string representation of a Square."""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.width)
