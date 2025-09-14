#!/usr/bin/python3

"""Simple tests for console.py"""

import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test console commands."""

    def test_prompt(self):
        """Test console prompt."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """Test empty line does nothing."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_quit(self):
        """Test quit command."""
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF command."""
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create_missing_class(self):
        """Test create without class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_create_invalid_class(self):
        """Test create with invalid class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create InvalidClass")
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_show_missing_class(self):
        """Test show without class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_show_invalid_class(self):
        """Test show with invalid class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show InvalidClass")
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_show_missing_id(self):
        """Test show without instance id."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
