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
    The State class is a Python class
    """
    name = ""
    def __init__(self, *args, **kwargs) -> None:
        from models import storage
        """
        This method inherits from BaseModel and is called when an instance 
        of the class state is created.

        Attributes:
        ----------------
        name = valid name of state
        """
        
        super().__init__(*args, **kwargs)
