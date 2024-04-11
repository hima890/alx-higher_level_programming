#!/usr/bin/python3
"""Defines a class Square"""


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the linked list.

    Methods:
        __init__(self, data, next_node=None): Initializes a Node object
        with data and optional next_node.
        data (property): Retrieves the data stored in the node.
        data.setter: Sets the data stored in the node with validation checks.
        next_node (property): Retrieves the reference to the next node.
        next_node.setter: Sets the reference to the next node with
        validation checks.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data stored in the node.

        Args:
            value (int): The data to set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the reference to the next node.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the reference to the next node.

        Args:
            value (Node or None): The reference to the next node.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Methods:
        __init__(self): Initializes an empty singly linked list.
        sorted_insert(self, value): Inserts a new Node into the correct sorted
        position in the list (increasing order).
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in
        the list (increasing order).

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            check = current.next_node and current.next_node.data < value
            while current.next_node is not None and check:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the singly linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
