#!/usr/bin/python3
"""Unit tests for City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_city_inherits_from_base_model(self):
        """Test that City inherits from BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_has_state_id_attribute(self):
        """Test that City has state_id attribute."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")

    def test_city_has_name_attribute(self):
        """Test that City has name attribute."""
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")

    def test_city_state_id_is_string(self):
        """Test that state_id is a string."""
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_city_name_is_string(self):
        """Test that name is a string."""
        city = City()
        self.assertIsInstance(city.name, str)

    def test_city_state_id_assignment(self):
        """Test that state_id can be assigned."""
        city = City()
        city.state_id = "1234-5678"
        self.assertEqual(city.state_id, "1234-5678")

    def test_city_name_assignment(self):
        """Test that name can be assigned."""
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_city_to_dict_contains_class(self):
        """Test that to_dict contains __class__ key."""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')

    def test_city_instance_creation(self):
        """Test that a City instance is created correctly."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
