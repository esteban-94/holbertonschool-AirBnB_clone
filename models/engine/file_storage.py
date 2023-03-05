#!/usr/bin/python3
"""
Module Name:
file_storage

Module Description:
This module contains only one Class

Module Classes:
- FileStorage

Module Attributes:
- None
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from os import path


class FileStorage():
    """
    This class is responsible for storing and retrieving
    objects from a JSON file.

    Attributes:

    __file_path: str - a private class attribute representing
                 the path to the JSON file.
    __objects: dict - a private class attribute representing
               the objects stored in the JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns a dictionary containing all of
        the objects stored in the JSON file.
        """
        return self.__objects

    def new(self, obj):
        """
        This method adds a new object to the dictionary of
        objects stored in the JSON file.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        This method saves the dictionary of objects to the JSON file.
        """
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as fl:
            json.dump(objects_dict, fl, indent=4)

    def reload(self):
        """
        This method loads the dictionary of objects from the JSON file.
        """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as fl:
                json_data = json.load(fl)
                for i in json_data.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            return
