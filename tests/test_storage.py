#!/usr/bin/python3
"""
file storage module
"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.city import City
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Class to test fileStorage"""

    def test_new_and_all_methods(self):
        """
        Check if the value return by all is a dict
        chekc if the key of the dict if the name of class
        associated with id.
        overall check all and new method with BaseModel class
        """
    
        my_model = BaseModel()
        all_objects = storage.all()
        self.assertEqual(type(all_objects), dict)
        for key, value in all_objects.items():
            class_name, obj_id = key.split(".")
            self.assertEqual(class_name, "BaseModel")








