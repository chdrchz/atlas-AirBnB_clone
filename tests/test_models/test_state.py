#!/usr/bin/python3
"""This module contains a set of unit tests for State"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class test for State"""

    def test_state(self):
        """Unit tests for State"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
