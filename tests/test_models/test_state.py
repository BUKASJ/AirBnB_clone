#!/usr/bin/python3
"""Unittests for State class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_attributes(self):
        """Test State class attributes."""
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_str_representation(self):
        """Test State class __str__ method."""
        state = State()
        state.id = "1234"
        state.name = "California"
        state_str = str(state)
        self.assertEqual(state_str, "[State] (1234) {'id': '1234', 'name': 'California'}")


if __name__ == "__main__":
    unittest.main()
