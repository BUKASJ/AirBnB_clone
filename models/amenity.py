#!/usr/bin/python3
"""Module for Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
