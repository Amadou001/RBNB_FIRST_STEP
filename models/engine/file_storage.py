#!/usr/bin/python3
"""
file_storage module
"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all: Method that return all the objects of a class

        Returns:
            dictionnary: dictionnary representation of all objects
        """
        return self.__objects

    def new(self, obj):
        """new: method to set in __objects the obj with key <obj class name>.id

        Args:
            obj (object): instance of a class
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """save: Method to save an object to a private class attribure __objects
        """
        all_objects = self.__objects
        dict_objects = {}
        for obj in all_objects.keys():
            dict_objects[obj] = all_objects[obj].to_dict()
        
        with open(self.__file_path, "w") as file:
            json.dump(dict_objects, file)

        
    def reload(self):
        """
            reload: method to deserialise an object from an existing file
            then save it to private class attribute __object
        """
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    content = json.load(file)
                    for key, value in content.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        class_instance = cls(**value)
                        self.__objects[key] = class_instance
            
            except Exception:
                pass
