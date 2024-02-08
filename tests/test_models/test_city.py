#!/usr/bin/python3
"""This module is a set of unit tests for User"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.city import City

my_model = City()

class TestCity(unittest.TestCase):
    """Class test City"""

    def test_city(self):
        """Unit tests for City"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
