#!/usr/bin/python3
"""Unit tests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_instance_creation(self):
        """Test that a BaseModel instance is created correctly."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_is_string(self):
        """Test that id is a string."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_id_is_unique(self):
        """Test that each instance has a unique id."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of BaseModel."""
        model = BaseModel()
        string = str(model)
        self.assertIn('[BaseModel]', string)
        self.assertIn(model.id, string)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute."""
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(0.1)
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict_returns_dict(self):
        """Test that to_dict() returns a dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all expected keys."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_class_name(self):
        """Test that __class__ key has correct value."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_to_dict_datetime_format(self):
        """Test that datetime attributes are strings in ISO format."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_create_from_dict(self):
        """Test creating an instance from a dictionary."""
        model1 = BaseModel()
        model1_dict = model1.to_dict()
        model2 = BaseModel(**model1_dict)
        self.assertEqual(model1.id, model2.id)
        self.assertEqual(model1.created_at, model2.created_at)
        self.assertEqual(model1.updated_at, model2.updated_at)

    def test_create_from_dict_different_instances(self):
        """Test that instances created from dict are different objects."""
        model1 = BaseModel()
        model1_dict = model1.to_dict()
        model2 = BaseModel(**model1_dict)
        self.assertIsNot(model1, model2)


if __name__ == '__main__':
    unittest.main()
