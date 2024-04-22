#!/usr/bin/python3
"""
console module
"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
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

    def test_save_method_without_storage(self):
        """Test save method without storage"""
        pass

    def test_to_dict(self):
        """Test to dict method"""
        pass




if __name__ == "__main__":
    unittest.main()




