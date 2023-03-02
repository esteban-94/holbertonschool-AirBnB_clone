import unittest
import json
import os
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """ Testing File Storae functionality """

    def setUp(self):
        """Set up"""
        self.file_path = 'file.json'
        self.obj1 = BaseModel()
        self.obj2 = User()
        self.obj1.save()
        self.obj2.save()

    def tearDown(self):
        """Tear down"""
        os.remove(self.file_path)

    def test_all(self):
        """Test all"""
        objs = storage.all()
        self.assertEqual(len(objs), 22)
        self.assertIn(f"{type(self.obj1).__name__}.{self.obj1.id}", objs)
        self.assertIn(f"{type(self.obj2).__name__}.{self.obj2.id}", objs)

    def test_new(self):
        """Test new"""
        obj3 = City()
        storage.new(obj3)
        objs = storage.all()
        self.assertEqual(len(objs), 25)
        self.assertIn(f"{type(obj3).__name__}.{obj3.id}", objs)

    def test_save(self):
        """Test save"""
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 29)
            self.assertIn(f"{type(self.obj1).__name__}.{self.obj1.id}", data)
            self.assertIn(f"{type(self.obj2).__name__}.{self.obj2.id}", data)
    
    def test_reload(self):
        """Test reload"""
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            del data[f"{type(self.obj1).__name__}.{self.obj1.id}"]
        with open(self.file_path, 'w') as f:
            json.dump(data, f)
        storage.reload()
        objs = storage.all()
        self.assertEqual(len(objs), 27)


if __name__ == '__main__':
    unittest.main()