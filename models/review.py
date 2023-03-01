"""
Module Name:
review

Module Description:
This module contains only one class

Module Classes:
- Review

Module Attributes:
- None
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
