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
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        all_objects = self.__objects
        dict_objects = {}
        for obj in all_objects.keys():
            dict_objects[obj] = all_objects[obj].to_dict()
        
        with open(self.__file_path, "w") as file:
            json.dump(dict_objects, file)

        
    def reload(self):
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    content = json.load(file)
                    for key, value in content.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        self.__objects[key] = instance
            
            except Exception:
                pass
        
    
    