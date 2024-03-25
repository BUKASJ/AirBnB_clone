#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def tearDown(self):
        """Clean test environment."""
        del self.model

    def test_instance_creation(self):
        """Test instance creation."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_id_generation(self):
        """Test id generation."""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """Test created_at attribute."""
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute."""
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method."""
        string = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), string)

    def test_save_method(self):
        """Test save method."""
        updated = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, updated)

    def test_to_dict_method(self):
        """Test to_dict method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_attribute_values(self):
        """Test to_dict method attribute values."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)

    def test_to_dict_created_at_format(self):
        """Test to_dict method created_at format."""
        model_dict = self.model.to_dict()
        self.assertEqual(
            model_dict['created_at'],
            self.model.created_at.isoformat()
        )

    def test_to_dict_updated_at_format(self):
        """Test to_dict method updated_at format."""
        model_dict = self.model.to_dict()
        self.assertEqual(
            model_dict['updated_at'],
            self.model.updated_at.isoformat()
        )

    def test_file_storage_linkage(self):
        """Test linkage of BaseModel to FileStorage."""
        self.assertTrue(os.path.exists('file.json'))


if __name__ == '__main__':
    unittest.main()
