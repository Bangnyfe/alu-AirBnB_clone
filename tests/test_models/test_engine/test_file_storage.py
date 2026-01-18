#!/usr/bin/python3
"""Unit tests for FileStorage class."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test fixtures."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() adds an object to storage."""
        model = BaseModel()
        self.storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that save() creates a file."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_loads_objects(self):
        """Test that reload() loads objects from file."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = f"BaseModel.{model.id}"
        self.assertIn(key, new_storage.all())


if __name__ == '__main__':
    unittest.main()
