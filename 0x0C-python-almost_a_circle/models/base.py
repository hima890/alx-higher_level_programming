#!/usr/bin/python3

import json


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)

    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)  # Update the dummy instance with the provided dictionary
        return dummy_instance
    
    @classmethod
    def load_from_file(cls):
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
