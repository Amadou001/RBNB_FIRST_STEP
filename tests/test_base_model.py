#!/usr/bin/python3
"""
console module
"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class to test basemodel module"""
    
    def test_create_object(self):
        """Check wether it's possible to create an object from BaseModel class"""
        my_new_modele = BaseModel()
        self.assertIsInstance(my_new_modele, BaseModel)

    def test_model_attributes_assignment(self):
        """Test model attributes assignment"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
    
    def test_kwargs_case(self):
        """Test kwargs case"""
        my_mode = BaseModel(name = "Antoine", age = 55)
        self.assertEqual(my_mode.name, "Antoine")
        self.assertEqual(my_mode.age, 55)
        

    def test_id_attribute(self):
        """Test all model class attribute"""
        my_new_model = BaseModel()
        uuid_obj = uuid.UUID(my_new_model.id)
        self.assertTrue(uuid.UUID(my_new_model.id, version=4))
        self.assertIsInstance(uuid_obj, uuid.UUID)

    def test_created_at_attribute(self):
        """Test created at attribute"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at_attribute(self):
        """Test updated at attribute"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)
        

    def test_str_representation(self):
        """Test str representation"""
        my_model = BaseModel()
        expected_output = f"[{my_model.__class__.__name__}] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_output)

    def test_str_repr_with_argument(self):
        """Test str with argument"""
        with self.assertRaises(AttributeError):
            my_model = BaseModel(name = "Antoine", age = 55)
            uuid_obj = uuid.UUID(my_model.id)
            self.assertTrue(uuid.UUID(my_model.id, version=4))
            self.assertIsInstance(uuid_obj, uuid.UUID)
    
    def test_to_dict_no_attribute(self):
        """Test to dict method"""
        my_model = BaseModel()
        my_model_dict_repr = my_model.to_dict()
        class_name = f"{my_model.__class__.__name__}"
        dictionary = my_model.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_to_dict_with_attribute(self):
        """Test to dict method"""
        my_model = BaseModel()
        my_model.name = "My first model"
        my_model.number = 33
        my_model_dict_repr = my_model.to_dict()
        class_name = f"{my_model.__class__.__name__}"
        dictionary = my_model.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_to_dict_value_as_list(self):
        my_model = BaseModel()
        my_model.my_list = [1, 2, 3]
        my_model.name = "First Model"
        my_model_dict_repr = my_model.to_dict()
        class_name = f"{my_model.__class__.__name__}"
        dictionary = my_model.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_to_dict_value_as_dict(self):
        my_model = BaseModel()
        my_model.my_dict = {"a": 1, "b": 2, "c": 3}
        my_model.name = "First Model"
        my_model_dict_repr = my_model.to_dict()
        class_name = f"{my_model.__class__.__name__}"
        dictionary = my_model.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_to_dict_value_as_tuple(self):
        my_model = BaseModel()
        my_model.my_tuple = (1, 2, 4)
        my_model.name = "First Model"
        my_model_dict_repr = my_model.to_dict()
        class_name = f"{my_model.__class__.__name__}"
        dictionary = my_model.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)


    def test_to_dict_with_kwargs(self):
        """Test to dict method"""
        with self.assertRaises(AttributeError):
            my_model = BaseModel(name = "My first model", number = 65)
            my_model_dict_repr = my_model.to_dict()
            class_name = f"{my_model.__class__.__name__}"
            dictionary = my_model.__dict__
            expected_dict = {"__class__": class_name}
            expected_dict.update(dictionary)

    def test_save_method_without_storage(self):
        """Test save method without storage"""
        my_model = BaseModel()
        my_model.save()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_update_at_created_at_assignemt(self):
        """test update_at and created_at"""
        with self.assertRaises(ValueError):
            my_model = BaseModel(created_at = "12pm", updated_at = "12pm")
            self.assertEqual(my_model.created_at, "12pm")

    

if __name__ == "__main__":
    unittest.main()




