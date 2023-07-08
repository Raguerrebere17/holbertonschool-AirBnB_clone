#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

dict_class = {
    'BaseModel': BaseModel,
    'User': user,
    'Place': place,
    'City': city,
    'Amenity': amenity,
    'Review': review
}

storage = FileStorage()
storage.reload()
