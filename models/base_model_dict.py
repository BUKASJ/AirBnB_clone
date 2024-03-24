#!/usr/bin/python3
"""
This module contains the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        Args:
            *args: Variable length argument list (unused).
            **kwargs: Arbitrary keyword arguments.
                Each key in kwargs is an attribute name.
                Each value in kwargs is the value of the corresponding attribute.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    continue
                elif key == "created_at":key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        Returns:
            String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        Returns:
            Dictionary representation of the BaseModel instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
