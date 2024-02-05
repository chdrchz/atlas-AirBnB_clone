#!/usr/bin/python3
"""This module contains unit tests for Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class test for Amenity"""

    def test_amenity(self):
        """Unit tests for Amenity"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, ""))
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
