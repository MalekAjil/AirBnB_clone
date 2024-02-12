#!/usr/bin/python3
"""
A BaseModel class that defines all common attributes/methods for other classes.
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Class initialization.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialing...
        Created_at, id, Updated_at and the time_format instance.
        Created_at, Updated_at are set to the isoformat using the
        .isoformat method.
        """
        DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = datetime.utcnow().isoformat()
        storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value,
                                                           DATE_TIME_FORMAT)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        private instance method.
        Prints the string representation of
        [<class name>] (<self.id>) <self.__dict__>
        """
        cls_name = self.__class__.__name__
        return f"[{cls_name}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dictionary_object = {}
        dictionary_object['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format strings
        if hasattr(self, 'created_at') and isinstance(self.created_at,
                                                      datetime):
            dictionary_object['created_at'] = self.created_at.isoformat()
        if hasattr(self, 'updated_at') and isinstance(self.updated_at,
                                                      datetime):
            dictionary_object['updated_at'] = self.updated_at.isoformat()

        dictionary_object.update(self.__dict__)

        return dictionary_object

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime.
        """
        self.updated_at = datetime.utcnow().isoformat()
        storage.save()
