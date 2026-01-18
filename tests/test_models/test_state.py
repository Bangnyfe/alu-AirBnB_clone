#!/usr/bin/python3
"""Unit tests for State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_state_inherits_from_base_model(self):
        """Test that State inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_has_name_attribute(self):
        """Test that State has name attribute."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
