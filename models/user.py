#!/usr/bin/python3
"""
Module Name: user
Module Description:
This module contains user class
Module Classes:
- User
Module Attributes:
- base_model.BaseModel
"""
from models import base_model
from datetime import datetime


class User(base_model.BaseModel):
    """
    The User class is a Python class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs) -> None:
        from models import storage
        """
        This method is called when an instance of the class user is created.

        Attributes:
        ----------------
        id
        """
        super().__init__(*args, **kwargs)
        storage.new(self)
