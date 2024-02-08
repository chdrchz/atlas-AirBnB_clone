#!/usr/bin/python3
"""This module is a set of unit tests for State"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.state import State

my_model = State()


class TestState(unittest.TestCase):
    """Class test for State"""

    def test_state(self):
        """Unit tests for State"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")
