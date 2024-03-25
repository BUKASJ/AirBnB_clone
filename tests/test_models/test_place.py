#!/usr/bin/python3
"""Unittests for Place class."""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_attributes(self):
        """Test Place class attributes."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_str_representation(self):
        """Test Place class __str__ method."""
        place = Place()
        place.id = "3456"
        place.name = "Beach House"
        place_str = str(place)
        self.assertEqual(place_str, "[Place] (3456) {'id': '3456', 'name': 'Beach House'}")


if __name__ == "__main__":
    unittest.main()
