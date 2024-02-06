#!/usr/bin/python3
"""This module is a set of unit tests for BaseModel"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

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

class TestAmenity(unittest.TestCase):
    """Class test for Amenity"""

    def test_amenity(self):
        """Unit tests for Amenity"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, ""))
        self.assertEqual(amenity.name, "")

class TestCity(unittest.TestCase):
    """Class test City"""

    def test_city(self):
        """Unit tests for City"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

        self.assertEqual(hasattr(city.state_id, ""))
        self.assertEqual(hasattr(city.name, ""))


class TestPlace(unittest.TestCase):
    """Class test for Place"""

    def test_place(self):
        """Unit tests for Place"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

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

class TestState(unittest.TestCase):
    """Class test for State"""

    def test_state(self):
        """Unit tests for State"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

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