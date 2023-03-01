#!/usr/bin/python3
"""Module file_storage"""


import json
from models.base_model import BaseModel
from models.user import User
from os import path


class FileStorage():
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as fl:
            json.dump(objects_dict, fl, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as fl:
                json_data = json.load(fl)
                self.__objects = {}
                for key, value in json_data.items():
                    self.__objects[key] = BaseModel(**value)
        else:
            pass
