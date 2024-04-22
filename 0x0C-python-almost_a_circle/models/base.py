#!/usr/bin/python3

import json


class Base:
    """Base class for creating instances with common attributes and methods.

    Attributes:
        __nb_objects (int): The number of objects created using this class.

    Methods:
        __init__(self, id=None): Initializes a new instance of the Base class.
        to_json_string(list_dictionaries): Converts a list of dictionaries to a
        JSON string.
        save_to_file(list_objs): Saves a list of objects to a JSON file.
        from_json_string(json_string): Converts a JSON string to a list of
        dictionaries.
        create(cls, **dictionary): Creates a new instance with attributes
        from a dictionary.
        load_from_file(cls): Loads a list of instances from a JSON file.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the Base class.

        Args:
            id (int, optional): The ID of the instance. If not provided,
            auto-increments the ID.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a JSON file.

        Args:
            list_objs (list): List of instances to be saved.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_str = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
                )
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to be converted.

        Returns:
            list: List of dictionaries extracted from the JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance with attributes from a dictionary.

        Args:
            **dictionary: Keyword arguments representing attributes of the new
            instance.

        Returns:
            Base: New instance of the class with attributes assigned from
            the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)  # Update the dummy instance with
        # the provided dictionary
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file.

        Returns:
            list: List of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                data = file.read()
                if data:
                    json_data = cls.from_json_string(data)
                    instances = [cls.create(**item) for item in json_data]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []
