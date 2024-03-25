#!/usr/bin/python3

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_attributes(self):
        """Test default attributes of User instance."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)


if __name__ == '__main__':
    unittest.main()
