#!/usr/bin/python3
# test_base.py
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):
    """
    Class test BaseModel
    """
    def test_save_to_file_json(self):
        """Test save()"""   
        # Setup
        storage = FileStorage()
        if os.path.exists("file.json"):
            os.remove("file.json")
        # Action
        storage.save()
        # Asserts
        self.assertTrue(os.path.exists("file.json"))
  
    def test_str_method(self):
        """Test the string representation."""
        inst = BaseModel(self)
        self.assertTrue(inst.__str__())
    
    def test_to_dict_exists(self):
        """Test that the to_dictionary method exists."""
        inst = BaseModel(self)
        expected = [inst.to_dict()]
        self.assertTrue(expected)