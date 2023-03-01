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
from os import path


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as fl:
            json.dump(objects_dict, fl, indent=4)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as fl:
                json_data = json.load(fl)
                for i in json_data.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        else:
            pass
