#!/usr/bin/python3
"""This module creates a city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

        Attributes:
        state_id(str): City id
        name(name): City name
    """

    state_id = ""
    name = ""
