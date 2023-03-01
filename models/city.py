#!/usr/bin/python3
"""
Module Name:
city

Module Description:
This module contains only one class

Module Classes:
- City

Module Attributes:
- None
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class inherits from the BaseModel class and
    represents a city within a state.

    Attributes:
    - id: str - a unique identifier generated using the uuid.uuid4() method.
    - created_at: datetime - the date and time when the instance was created,
                  set using the datetime.now() method.
    - updated_at: datetime - the date and time when the instance was
                  last updated, set using the datetime.now() method.
    - state_id: str - the unique identifier of the state
                that the city belongs to.
    - name: str - the name of the city.

    Methods:
    - __init__(*args, **kwargs) -> None
        This method is called when an instance of the class is created.
        It initializes the instance's attributes id, created_at,
        updated_at, state_id, and name.

    - __str__() -> str
        This method returns a string representation of the instance.
        The string includes the instance's class name, id, state_id,
        and name attribute.

    - to_dict() -> dict
        This method returns a dictionary representation of the instance.
        The dictionary includes all of the instance's attributes,
        as well as the class name, created_at, and updated_at attributes.
        he created_at and updated_at attributes are formatted as ISO 8601
        strings using the datetime.isoformat() method.
    """
    state_id = ""
    name = ""
