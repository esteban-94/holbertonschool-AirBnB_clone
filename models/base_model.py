#!/usr/bin/python3
"""
Module Name: base_model
Module Description:
This module contains only one Class
Module Classes:
- BaseModel
Module Attributes:
- None
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    The BaseModel class is a Python class that can be used as a base class
    for other classes that require common functionality such as creating a
    unique ID, saving to a database, and converting to a dictionary.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        This method is called when an instance of the class is created.
        It initializes the instance's attributes id, created_at, and updated_at

        Attributes:
        ----------------
        id: is a unique identifier generated using the uuid.uuid4() method.
        created_at and updated_at: are set to the current date and time
                                   using the datetime.now() method.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """
        This method returns a string representation of the instance.
        The string includes the instance's class name, id, and attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        This method updates the updated_at attribute to the current date
        and time using the datetime.now() method. It can be used to indicate
        that an instance has been modified and needs to be saved.
        """
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        This method returns a dictionary representation of the instance.
        The dictionary includes all of the instance's attributes,
        as well as the class name, created_at, and updated_at attributes.
        The created_at and updated_at attributes are formatted as ISO 8601
        strings using the datetime.isoformat() method.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
