import unittest
from datetime import datetime
import uuid

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Create an instance to check
        self.base_model = BaseModel()

    def test_id_is_valid_uuid(self):
        # Check that the id attribute is a valid UUID
        self.assertIsInstance(uuid.UUID(self.base_model.id), uuid.UUID)

    def test_created_at_is_datetime(self):
        # Check that the created_at attribute is a datetime object
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        # Check that the updated_at attribute is a datetime object
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        # Check that calling the save method updates the updated_at attribute
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)

    def test_to_dict_includes_all_attributes(self):
        # Check that the to_dict method returns a dictionary with all attributes
        dict_copy = self.base_model.to_dict()
        self.assertIn('id', dict_copy)
        self.assertIn('created_at', dict_copy)
        self.assertIn('updated_at', dict_copy)

    def test_to_dict_includes_class_name(self):
        # Check that the to_dict method returns a dictionary with the class name
        dict_copy = self.base_model.to_dict()
        self.assertIn('__class__', dict_copy)
        self.assertEqual(dict_copy['__class__'], 'BaseModel')

    def test_to_dict_includes_created_at_isoformat(self):
        # Check that the to_dict method returns a dictionary with the created_at attribute as an ISO 8601 string
        dict_copy = self.base_model.to_dict()
        self.assertEqual(dict_copy['created_at'], self.base_model.created_at.isoformat())

    def test_to_dict_includes_updated_at_isoformat(self):
        # Check that the to_dict method returns a dictionary with the updated_at attribute as an ISO 8601 string
        dict_copy = self.base_model.to_dict()
        self.assertEqual(dict_copy['updated_at'], self.base_model.updated_at.isoformat())

    def test_str_returns_correct_string(self):
        # Check that the __str__ method returns the correct string
        expected_string = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_string)

if __name__ == '__main__':
    unittest.main()
