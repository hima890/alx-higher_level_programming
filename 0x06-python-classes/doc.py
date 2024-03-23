# my_module.py

class MyClass:
    """
    This is a simple class to demonstrate documentation.
    
    Attributes:
    - attribute1: A string attribute
    - attribute2: An integer attribute
    """

    def __init__(self, attribute1="default", attribute2=0):
        """
        Constructor for MyClass.

        Parameters:
        - attribute1 (str): Value for attribute1 (default is "default").
        - attribute2 (int): Value for attribute2 (default is 0).
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def my_method(self):
        """
        This is a method of MyClass.

        It simply prints the values of attribute1 and attribute2.
        """
        print(f"attribute1: {self.attribute1}, attribute2: {self.attribute2}")

def my_function(x, y):
    """
    This is a simple function to demonstrate documentation.

    Parameters:
    - x (int): First parameter.
    - y (int): Second parameter.

    Returns:
    - int: The sum of x and y.
    """
    return x + y
