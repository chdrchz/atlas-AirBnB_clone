#!/usr/bin/python3
"""This module is a set of unit tests for BaseModel"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


my_model = BaseModel()


class TestBaseModel(unittest.TestCase):
    """Class test BaseModel"""

    def test_id(self):
        """Unittest that tests id"""
        self.assertTrue(type(my_model.id) is str)
    
    def test_created_at(self):
        """Unittest that tests created_at method"""
        self.assertTrue(type(my_model.created_at) is datetime)
    
    def test_str(self):
        """Unittest that tests str formatting"""
        self.assertEqual(str(my_model), "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.to_dict()))
    
    def test_to_dict(self):
        """ Unittest that tests to_dict method """
        my_dict = my_model.to_dict()
        self.assertTrue(type(my_dict["created_at"]) is str)
        self.assertTrue(type(my_dict) is dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertIn("__class__", my_dict.keys())

    def test_save(self):
        """Unittest that tests save method"""
        my_save = my_model.updated_at
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))
        my_save2 = my_model.updated_at
        self.assertNotEqual(my_save, my_save2)
