#!/usr/bin/python3
"""Unit tests for Console class."""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for Console class."""

    def setUp(self):
        """Set up test fixtures."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_quit_command(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF_command(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_missing_class(self):
        """Test create command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
