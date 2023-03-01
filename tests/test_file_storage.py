import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_all(self):
        #Test all method
        fs1 = FileStorage()
        fs2 = FileStorage()
        self.assertEqual(fs1.all(), fs2.all())

    def test_new(self):
        #Test new method
        fs1 = FileStorage()
        bm1 = BaseModel()
        fs1.new(bm1)
        self.assertEqual(fs1.all(), {f'BaseModel.{bm1.id}': bm1})

    def test_save(self):
        #Test save method
        fs1 = FileStorage()
        bm1 = BaseModel()
        fs1.new(bm1)
        fs1.save()
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 2)
            self.assertIn(f'BaseModel.{bm1.id}', data)


if __name__ == '__main__':
    unittest.main()