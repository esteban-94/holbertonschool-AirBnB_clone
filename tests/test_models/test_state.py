import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Testing State functionality """

    def setUp(self):
        """Set up"""
        self.state = State()

    def test_name(self):
        """Test name"""
        self.assertEqual(self.state.name, '')

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'id'))

    def test_attribute_defaults(self):
        """Test attribute defaults"""
        self.assertEqual(self.state.name, '')

    def test_str(self):
        """Test str"""
        expected = f"[{type(self.state).__name__}] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected)


if __name__ == '__main__':
    unittest.main()