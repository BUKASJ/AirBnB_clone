#!/usr/bin/python3
"""Module for Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
