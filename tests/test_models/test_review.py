#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testing Review functionality """

    def setUp(self):
        """Set up"""
        self.review = Review()

    def test_place_id(self):
        """Test place_id"""
        self.assertEqual(self.review.place_id, '')

    def test_user_id(self):
        """Test user_id"""
        self.assertEqual(self.review.user_id, '')

    def test_text(self):
        """Test text"""
        self.assertEqual(self.review.text, '')

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'id'))

    def test_attribute_defaults(self):
        """Test attribute defaults"""
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')

    def test_str(self):
        """Test str"""
        expected = f"[{type(self.review).__name__}] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected)


if __name__ == '__main__':
    unittest.main()