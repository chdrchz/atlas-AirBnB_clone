#!/usr/bin/python3

import unittest
import json
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """This is the unittest for File Storage"""
    def setUp(self):
        """This method is the set up for testing"""
        self.file_path = "file_test.json"
        storage.__file_path = self.file_path
        self.storage = FileStorage()
        self.obj = BaseModel()
    
    def tearDown(self):
        """This cleans up after testing"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """This tests the all method"""
        all_objects = self.storage.all()
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.storage.new(self.obj)
        all_objects = self.storage.all()
        self.assertEqual(all_objects[key], self.obj)
    
    def test_new(self):
        """This tests the new method"""
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.storage.new(self.obj)
        self.assertIn(key, self.storage.all())
    
    def test_update(self):
        """This tests the update method"""
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.storage.new(self.obj)
        new_value = "new_value"
        self.storage.update(self.obj, 'test_attribute', new_value)
        updated_object = self.storage.all()[key]
        self.assertEqual(getattr(updated_object, 'test_attribute'), new_value)

    def test_remove(self):
        """This tests the remove method"""
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.storage.new(self.obj)
        self.storage.remove(key)
        self.assertNotIn(key, self.storage.all())
    
    def test_save_and_reload(self):
        """This tests the save and reload methods"""
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.storage.new(self.obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        reloaded_object = new_storage.all()[key]
        self.assertEqual(reloaded_object.id, self.obj.id)
        self.assertEqual(reloaded_object.to_dict(), self.obj.to_dict())

    if __name__ == '__main__':
        unittest.main()