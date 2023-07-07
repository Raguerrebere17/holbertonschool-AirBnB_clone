#!/usr/bin/python3
"""
class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    class BaseModel attributes
    id: uuid
    created_at: date
    updated_at: date
    """
    def __init__(self):
        """
        creates new instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string method

        Returns:
            string: instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save data
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict function

        return instance as dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict