#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for the console.py module."""

    @classmethod
    def setUpClass(cls):
        """Set up testing environment."""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Tear down testing environment."""
        del cls.console

    def setUp(self):
        """Redirect stdout to a StringIO object."""
        self.console.stdout = StringIO()

    def tearDown(self):
        """Clean up after each test."""
        self.console.stdout = sys.stdout

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)
            self.assertTrue(output == storage.all()["BaseModel." + output].id)

    def test_create_missing_class_name(self):
        """Test create command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class_name(self):
        """Test create command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show(self):
        """Test show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel " + id)
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_show_missing_class_name(self):
        """Test show command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_invalid_class_name(self):
        """Test show command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_missing_instance_id(self):
        """Test show command with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_instance_id(self):
        """Test show command with invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel " + id)
            output = f.getvalue().strip()
            self.assertFalse(output)
            self.assertNotIn(id, storage.all())

    def test_destroy_missing_class_name(self):
        """Test destroy command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_invalid_class_name(self):
        """Test destroy command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_missing_instance_id(self):
        """Test destroy command with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_invalid_instance_id(self):
        """Test destroy command with invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_all_invalid_class_name(self):
        """Test all command with invalid class name."""
        with patch('sys.stdout', new=StringIO
