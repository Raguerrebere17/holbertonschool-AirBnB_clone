#!/usr/bin/python3
import json
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
        """_summary_
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                class_ = globals()[class_name]
                instance = class_()

                for attr, val in value.items():
                    setattr(instance, attr, val)

                self.__objects[keys] = instance

        except FileNotFoundError:
            pass