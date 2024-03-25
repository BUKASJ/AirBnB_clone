#!/usr/bin/python3
"""Unittests for Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_attributes(self):
        """Test Amenity class attributes."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_str_representation(self):
        """Test Amenity class __str__ method."""
        amenity = Amenity()
        amenity.id = "9012"
        amenity.name = "Wifi"
        amenity_str = str(amenity)
        self.assertEqual(amenity_str, "[Amenity] (9012) {'id': '9012', 'name': 'Wifi'}")


if __name__ == "__main__":
    unittest.main()
