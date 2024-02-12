#!/usr/bin/python3
"""
Module for serializing and deserializing data into JSON format
and back from JSON format
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class for storing, serializing and deserializing JSON Data
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        class_name = obj.__class__.__name__
        if obj:
            key = '{}.{}'.format(class_name, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()
        
        try:
            with open(self.__file_path, 'w') as f:
                json.dump(serialized_objs, f)
        except Exception as e:
            print(f"Error occurred while saving: {e}")

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file exists;
        otherwise, do nothing. If the file doesn’t exist.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
                for key, val in data.items():
                    obj = self.class_dict[val["__class__"]](**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

