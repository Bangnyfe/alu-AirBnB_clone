#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all models in the AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance.

        Args:
            *args: Unused positional arguments.
            **kwargs: Key-value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance.

        Returns:
            str: String in format [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert instance to dictionary representation.

        Returns:
            dict: Dictionary containing all keys/values of __dict__.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
