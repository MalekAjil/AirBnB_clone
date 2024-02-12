#!/usr/bin/python3
"""
Module for serializing and deserializing data into JSON format
and back from JSON format
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    A class for storing, serializing and deserializing JSON Data
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        class_name = obj.to_dict()['__class__']
        id_key = obj.id
        self.all()[f"{class_name}.{id_key}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump({x: y.to_dict() for x, y in self.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file exists;
        otherwise, do nothing. If the file doesn’t exist.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    obj_class = classes.get(val['__class__'])
                    if obj_class:
                        obj_instance = obj_class(**val)
                        self.all()[key] = obj_instance
        except FileNotFoundError:
            pass
