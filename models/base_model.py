#!/usr/bin/python3
"""
Base model module
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base model class
        Instance attributes:
            id (str): unique id for each BaseModel
            created_at (date): current datetime when an instance is created
            updated_at (date): current datetime when an instance is created
                     and it will be updated every time you change your object
    """
    def __init__(self, *args, **kwargs): 
        """
        Constructor

            Args:
                args: (unused):
                kwargs (dictionary): only the "class" key will not
                        be added as attribute of the object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    
                    if key == "created_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
                    elif key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the object
        """
        object_class = type(self)
        return "[{}] ({}) {}".format(object_class.__name__, self.id, self.__dict__)
        
    
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        current_time = datetime.now()
        self.updated_at = current_time
        models.storage.save()
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of dict of the instance
        """
        if isinstance(self.created_at, datetime) and isinstance(self.updated_at, datetime):
            self.created_at = self.created_at.isoformat()
            self.updated_at = self.updated_at.isoformat()
        diction = self.__dict__
        object_class = type(self)
        diction2 = {'__class__': f'{object_class.__name__}'}
        diction.update(diction2)
        return diction
