"""
Module Name:
place

Module Description:
This module contains only one class

Module Classes:
- Place

Module Attributes:
- None
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place class is a Python class that inherits from the BaseModel class.

    Attributes:
    - city_id: a string representing the id of the City
               instance in which the place is located.
    - user_id: a string representing the id of the User
               instance that owns the place.
    - name: a string representing the name of the place.
    - description: a string representing the description of the place.
    - number_rooms: an integer representing the number of rooms in the place.
    - number_bathrooms: an integer representing the number of
                        bathrooms in the place.
    - max_guest: an integer representing the maximum number
                 of guests the place can accommodate.
    - price_by_night: an integer representing the price per
                      night to stay at the place.
    - latitude: a float representing the latitude of the place's location.
    - longitude: a float representing the longitude of the place's location.
    - amenity_ids: a list of strings representing the ids of the Amenity
                   instances that are associated with the place.

    Methods:
    - __init__(self, *args, kwargs) -> None
        Constructor method that initializes the attributes of the class.
        Calls the constructor of the parent class BaseModel and creates
        the Place instance.
    - __str__() -> str
        Method that returns a string representation of the instance.
    - to_dict() -> dict
        Method that returns a dictionary representation of the instance.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
