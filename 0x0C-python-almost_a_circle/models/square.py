#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class and represents
    a square shape.

    Attributes:
        size (int): The size of the square (both width and height).
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): The ID of the square.

    Methods:
        update(self, *args, **kwargs): Updates the attributes of
        the square.
        __str__(self): Returns the string representation of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int, optional): The x-coordinate of the top-left
            corner of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left
            corner of the square. Defaults to 0.
            id (int, optional): The ID of the square. Defaults
            to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )

    @property
    def size(self):
        """int: The size of the square (both width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square (both width and height).

        Args:
            value (int): The size value to set.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
