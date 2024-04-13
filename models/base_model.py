#!/usr/bin/python3
"""
Base model module
"""

import uuid
import datetime

class BaseModel:
    """
    Base model class
        Instance attributes:
            id (str): unique id for each BaseModel
            created_at (date): current datetime when an instance is created
            updated_at (date): current datetime when an instance is created
                     and it will be updated every time you change your object
    """
    def __init__(self):
        """
        Constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns the string representation of the object
        """
        object_class = type(self)
        return f"{[object_class.__name__]} ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        current_time = datetime.datetime.now()
        self.updated_at = current_time.isoformat()
        self.created_at = self.created_at.isoformat()
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        diction = self.__dict__
        object_class = type(self)
        diction2 = {'__class__': f'{object_class.__name__}'}
        diction.update(diction2)
        return diction
    