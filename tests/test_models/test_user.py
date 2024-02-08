#!/usr/bin/python3
"""This module is a set of unit tests for User"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User

my_model = User()

class TestUser(unittest.TestCase):
    """Class tests for User"""

    def test_user(self):
        """Unit tests for User"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()