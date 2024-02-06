#!/usr/bin/python3
"""This module defines a class named BaseModel"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """This is the base class named BaseModel"""
    def __init__(self, *args, **kwargs):
        """Public instantation method"""
        from models import storage

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else: 
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation method"""
        return("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Updates the updated_at attribute with the current datetime and saves"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """Returns a dict of all instances created"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data