#!/usr/bin/python3
"""Unit tests for User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_user_inherits_from_base_model(self):
        """Test that User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_has_attributes(self):
        """Test that User has required attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_attributes_are_strings(self):
        """Test that User attributes are empty strings by default."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_email_assignment(self):
        """Test that email can be assigned."""
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")


if __name__ == '__main__':
    unittest.main()
