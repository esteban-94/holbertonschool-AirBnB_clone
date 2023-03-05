#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Testing Amenity functionality """

    def setUp(self):
        """Set up"""
        self.amenity = Amenity()

    def test_name(self):
        """Test name"""
        self.assertEqual(self.amenity.name, '')

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'id'))

    def test_attribute_defaults(self):
        """Test attribute defaults"""
        self.assertEqual(self.amenity.name, '')

    def test_str(self):
        """Test str"""
        expected = f"[{type(self.amenity).__name__}] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected)


if __name__ == '__main__':
    unittest.main()