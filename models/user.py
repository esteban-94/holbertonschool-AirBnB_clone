#!/usr/bin/python3
"""
Module Name:
user

Module Description:
This module contains only one class

Module Classes:
- User

Module Attributes:
- None
"""
from models.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
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
        This method inherits from BaseModel and is called when an instance 
        of the class user is created.

        Attributes:
        ----------------
        email = valid email of user
        password = valid password of user
        first_name = valid first name of user
        last_name = valid last name of user
        """
        
        super().__init__(*args, **kwargs)
        storage.new(self)
