#!/usr/bin/python3
"""BaseModel module defining the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel defines common attributes/methods for other classes.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Timestamp of instance creation.
        updated_at (datetime): Timestamp of last update.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance.
        If kwargs is empty, generates new id and timestamps.
        If kwargs is provided, sets attributes from kwargs.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            return

        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key in ["created_at", "updated_at"]:
                try:
                    casted_time = datetime.fromisoformat(value)
                    setattr(self, key, casted_time)
                    continue
                except Exception:
                    raise Exception("date time is not iso format")
            if key == "id":
                setattr(self, key, str(value))
            else:
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [ClassName] (id) {attribute_dict}
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.__dict__}"
        )

    def save(self):
        """
        Updates updated_at to current time and saves instance to storage.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary of instance attributes.
        Converts datetime attributes to ISO format strings.
        """
        obj = {}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                obj[key] = value.isoformat()
                continue
            obj[key] = value
        return obj
