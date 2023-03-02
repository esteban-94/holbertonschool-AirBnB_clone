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


class User(BaseModel):
    """
    This class inherits from the BaseModel class and represents a user.

    Attributes:
    - id: str - a unique identifier generated using the uuid.uuid4() method.
    - created_at: datetime - the date and time when the instance was created,
                  set using the datetime.now() method.
    - updated_at: datetime - the date and time when the instance was
                  last updated, set using the datetime.now() method.
    - email: str - the email address of the user.
    - password: str - the password of the user.
    - first_name: str - the first name of the user.
    - last_name: str - the last name of the user.

    Methods:
    - __init__(*args, **kwargs) -> None
        This method is called when an instance of the class is created.
        It initializes the instance's attributes id, created_at, updated_at,
        email, password, first_name, and last_name.

    - __str__() -> str
        This method returns a string representation of the instance.
        The string includes the instance's class name, id, email, first_name,
        and last_name attribute.

    - to_dict() -> dict
        This method returns a dictionary representation of the instance.
        The dictionary includes all of the instance's attributes,
        as well as the class name, created_at, and updated_at attributes.
        The created_at and updated_at attributes are formatted as ISO 8601
        strings using the datetime.isoformat() method.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
