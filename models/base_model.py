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
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            return
        for key, value in kwargs:
            if key not in ["arg"]:
                raise Exception(f"{key} is not allowed")
            self[key] = value

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [ClassName] (id) {attribute_dict}
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at timestamp to current time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary of the instance attributes.
        Converts datetime attributes to ISO format strings.
        """
        obj = {}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                obj.__setitem__(key, value.isoformat())
                continue
            obj[key] = value

        return obj
