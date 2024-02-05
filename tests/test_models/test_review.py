#!/usr/bin/python3
"""This module contains unit tests for Review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class tests Review"""

    def test_review(self):
        """Unit tests for Review"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
