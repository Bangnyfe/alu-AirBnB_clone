#!/usr/bin/python3
"""Unit tests for Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_place_inherits_from_base_model(self):
        """Test that Place inherits from BaseModel."""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_has_city_id_attribute(self):
        """Test that Place has city_id attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")

    def test_place_has_user_id_attribute(self):
        """Test that Place has user_id attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, "")

    def test_place_has_name_attribute(self):
        """Test that Place has name attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")

    def test_place_has_description_attribute(self):
        """Test that Place has description attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, "")

    def test_place_has_number_rooms_attribute(self):
        """Test that Place has number_rooms attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(place.number_rooms, 0)

    def test_place_has_number_bathrooms_attribute(self):
        """Test that Place has number_bathrooms attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(place.number_bathrooms, 0)

    def test_place_has_max_guest_attribute(self):
        """Test that Place has max_guest attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertEqual(place.max_guest, 0)

    def test_place_has_price_by_night_attribute(self):
        """Test that Place has price_by_night attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(place.price_by_night, 0)

    def test_place_has_latitude_attribute(self):
        """Test that Place has latitude attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertEqual(place.latitude, 0.0)

    def test_place_has_longitude_attribute(self):
        """Test that Place has longitude attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertEqual(place.longitude, 0.0)

    def test_place_has_amenity_ids_attribute(self):
        """Test that Place has amenity_ids attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.amenity_ids, [])

    def test_place_city_id_is_string(self):
        """Test that city_id is a string."""
        place = Place()
        self.assertIsInstance(place.city_id, str)

    def test_place_user_id_is_string(self):
        """Test that user_id is a string."""
        place = Place()
        self.assertIsInstance(place.user_id, str)

    def test_place_name_is_string(self):
        """Test that name is a string."""
        place = Place()
        self.assertIsInstance(place.name, str)

    def test_place_description_is_string(self):
        """Test that description is a string."""
        place = Place()
        self.assertIsInstance(place.description, str)

    def test_place_number_rooms_is_int(self):
        """Test that number_rooms is an integer."""
        place = Place()
        self.assertIsInstance(place.number_rooms, int)

    def test_place_number_bathrooms_is_int(self):
        """Test that number_bathrooms is an integer."""
        place = Place()
        self.assertIsInstance(place.number_bathrooms, int)

    def test_place_max_guest_is_int(self):
        """Test that max_guest is an integer."""
        place = Place()
        self.assertIsInstance(place.max_guest, int)

    def test_place_price_by_night_is_int(self):
        """Test that price_by_night is an integer."""
        place = Place()
        self.assertIsInstance(place.price_by_night, int)

    def test_place_latitude_is_float(self):
        """Test that latitude is a float."""
        place = Place()
        self.assertIsInstance(place.latitude, float)

    def test_place_longitude_is_float(self):
        """Test that longitude is a float."""
        place = Place()
        self.assertIsInstance(place.longitude, float)

    def test_place_amenity_ids_is_list(self):
        """Test that amenity_ids is a list."""
        place = Place()
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_attributes_assignment(self):
        """Test that attributes can be assigned."""
        place = Place()
        place.city_id = "city-123"
        place.user_id = "user-456"
        place.name = "Beautiful Apartment"
        place.description = "A lovely place to stay"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["amenity-1", "amenity-2"]

        self.assertEqual(place.city_id, "city-123")
        self.assertEqual(place.user_id, "user-456")
        self.assertEqual(place.name, "Beautiful Apartment")
        self.assertEqual(place.description, "A lovely place to stay")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity-1", "amenity-2"])

    def test_place_to_dict_contains_class(self):
        """Test that to_dict contains __class__ key."""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_place_instance_creation(self):
        """Test that a Place instance is created correctly."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
