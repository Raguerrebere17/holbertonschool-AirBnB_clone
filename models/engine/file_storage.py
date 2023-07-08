#!/usr/bin/python3
import os
import sys
import json
import models
import importlib
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
        Deserializes the JSON file to __objects
        """
    if os.path.isfile(self.__file_path):
        with open(self.__file_path, 'r') as file:
            obj_dict = json.load(file)

        for key, value in obj_dict.items():
            class_name, obj_id = key.split('.')
            if class_name == "User":
                class_ = User
            elif class_name == "State":
                class_ = State
            elif class_name == "City":
                class_ = City
            elif class_name == "Amenity":
                class_ = Amenity
            elif class_name == "Place":
                class_ = Place
            elif class_name == "Review":
                class_ = Review
            else:
                continue

            instance = class_(**value)
            self.__objects[key] = instance

