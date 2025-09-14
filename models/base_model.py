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
            # Add new instance to storage
            from models import storage
            storage.new(self)
            return
        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if (key in ["created_at", "updated_at"]):
                if value is None:
                    raise TypeError(f"{key} cannot be None")
                try:
                    casted_time = datetime.fromisoformat(value)
                    setattr(self, key, casted_time)
                    continue
                except:
                    raise Exception(f"date time is not iso format")

            if key == "id":
                if value is None:
                    raise TypeError("id cannot be None")
                setattr(self, key, str(value))
            else:
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [ClassName] (id) {attribute_dict}
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at timestamp to current time
          and saves the instance to storage.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

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

        # Add class name
        obj["__class__"] = self.__class__.__name__
        return obj
