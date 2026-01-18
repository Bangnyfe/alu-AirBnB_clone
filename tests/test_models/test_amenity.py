#!/usr/bin/python3
"""Unit tests for Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_amenity_inherits_from_base_model(self):
        """Test that Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_has_name_attribute(self):
        """Test that Amenity has name attribute."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_amenity_name_is_string(self):
        """Test that name is a string."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_name_assignment(self):
        """Test that name can be assigned."""
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_to_dict_contains_class(self):
        """Test that to_dict contains __class__ key."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_amenity_instance_creation(self):
        """Test that an Amenity instance is created correctly."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_amenity_str_representation(self):
        """Test the string representation of Amenity."""
        amenity = Amenity()
        string = str(amenity)
        self.assertIn('[Amenity]', string)
        self.assertIn(amenity.id, string)


if __name__ == '__main__':
    unittest.main()
