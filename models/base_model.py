#!/usr/bin/python3
"""This module defines a class named BaseModel"""
from datetime import datetime
import uuid


class BaseModel:
    """This is the base class named BaseModel"""

    def __init__(self):
        """Public instantation method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation method"""
        print("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Returns a dict of all instances created"""
        result = self.__dict__.copy()
        result['__class__'] = type(self).__name__
        if 'created_at' in result and isinstance(result['created_at'], datetime):
            result['created_at'] = result['created_at'].isoformat()
        if 'updated_at' in result and isinstance(result['updated_at'], datetime):
            result['updated_at'] = result['updated_at'].isoformat()
        return result