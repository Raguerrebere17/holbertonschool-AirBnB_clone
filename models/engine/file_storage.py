#!/usr/bin/python3
import os
import sys
import json
import models
import importlib
from models.base_model import BaseModel
from models.user import User
"""
    class FileStorage
"""


class FileStorage:
    """
    class FileStorage

    __file_path = json
    __objects = dict
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        return self.__objects

    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """_summary_
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        A method deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(self.__file_path, mode="r+", encoding="UTF-8") as f:
                data = json.load(f)
            for key, value in data.items():
                class_obj = value.get('__class__')
                if class_obj in models.dict_class:
                    if class_obj == "User":
                        self.__objects[key] = User(**value)
                    else:
                        self.__objects[key] = models.dict_class[class_obj](**value)
