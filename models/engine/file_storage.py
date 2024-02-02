#!/usr/bin/python3
"""This module defines a class named FileStorage"""
import json
import os


class FileStorage():
    """This class serializes and deserializes instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """This method sets keys and values for a dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """This method serializes __objects to the JSON file"""
        serial_objects = {}
        for key, obj in self.__objects.items():
            serial_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serial_objects, f)

    def reload(self):
        """This method deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        try: 
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    obj = eval(obj_dict['__class__'])(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
