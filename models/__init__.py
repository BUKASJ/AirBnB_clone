#!/usr/bin/python3
"""Module for storing instances of the classes."""
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class_dict = {"BaseModel": BaseModel, "User": User}

storage = FileStorage()
storage.reload()
