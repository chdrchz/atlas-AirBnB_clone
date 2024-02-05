#!/usr/bin/python3
"""This module is a set of tests for City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class test City"""

    def test_city(self):
        """Unit tests for City"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

        self.assertEqual(hasattr(city.state_id, ""))
        self.assertEqual(hasattr(city.name, ""))

if __name__ == '__main__':
    unittest.main()
