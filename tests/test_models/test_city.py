#!/usr/bin/python3
"""Unittests for City class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_attributes(self):
        """Test City class attributes."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_str_representation(self):
        """Test City class __str__ method."""
        city = City()
        city.id = "5678"
        city.state_id = "1234"
        city.name = "San Francisco"
        city_str = str(city)
        self.assertEqual(city_str, "[City] (5678) {'id': '5678', 'state_id': '1234', 'name': 'San Francisco'}")


if __name__ == "__main__":
    unittest.main()
