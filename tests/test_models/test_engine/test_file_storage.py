import inspect
import json
import os
import unittest

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Testing the FileStorage class of the program.
        """

    def setUp(self):
        """ Method to prepare each single test.
            """
        self.storage_test = FileStorage()
        self.path = self.storage_test._FileStorage__file_path
        if os.path.exists(self.path):
            os.rename(self.path, "original_{}".format(self.path))

    def test_module_documentation(self):
        """ Test if FileStorage module is documented.
            """
        self.assertTrue(FileStorage.__doc__)

    def test_class_documentation(self):
        """ Test if FileStorage class is documented.
            """
        self.assertTrue(FileStorage.__doc__)

    def test_methods_documentation(self):
        """ Test if all FileStorage methods are documented.
            """
        methods = inspect.getmembers(FileStorage)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic FileStorage instances.
            """
        self.assertIsInstance(self.storage_test, FileStorage)

    def test_save_method(self):
        """ Check the save() method.
            """
        base_model_test = BaseModel()
        self.storage_test.save()
        self.assertTrue(os.path.exists(self.path))
        with open(self.path) as file:
            file_dict = json.load(file)
        self.assertIn(base_model_test.to_dict(), file_dict.values())

    def test_reload_method(self):
        """ Check the reload() method.
            """
        base_model_test = BaseModel()
        self.storage_test.save()
        self.storage_test.reload()
        key_to_search = "BaseModel.{}".format(base_model_test.id)
        file_dict = self.storage_test.all()
        self.assertFalse(file_dict[key_to_search] is base_model_test)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists(self.path):
            os.remove(self.path)
        if os.path.exists("original_{}".format(self.path)):
            os.rename("original_{}".format(self.path), self.path)

    def save(self):
        """this method serialize a dict and
        the write a in file .json
        """
        dic = {}
        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dic, f)