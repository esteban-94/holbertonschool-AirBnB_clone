#!/usr/bin/python3
"""
Module Name:
state

Module Description:
This module contains only one class

Module Classes:
- State

Module Attributes:
- None
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class inherits from the BaseModel class and represents a state.

    Attributes:
    - id: str - a unique identifier generated using the uuid.uuid4() method.
    - created_at: datetime - the date and time when the instance was created,
                  set using the datetime.now() method.
    - updated_at: datetime - the date and time when the instance was last updated,
                  set using the datetime.now() method.
    - name: str - the name of the state.

    Methods:

    - init(*args, **kwargs) -> None
        This method is called when an instance of the class is created.
        It initializes the instance's attributes id, created_at, updated_at, and name.
    - str() -> str
        This method returns a string representation of the instance.
        The string includes the instance's class name, id, and name attribute.
    - to_dict() -> dict
        This method returns a dictionary representation of the instance.
        The dictionary includes all of the instance's attributes, as well as the class name,
        created_at, and updated_at attributes. The created_at and updated_at attributes are
        formatted as ISO 8601 strings using the datetime.isoformat() method.
    """
    name = ""
