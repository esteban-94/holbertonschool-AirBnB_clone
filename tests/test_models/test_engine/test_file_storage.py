import inspect
import json
import os
import unittest

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        self.storage_test.new(bm)
        self.storage_test.new(us)
        self.storage_test.new(st)
        self.storage_test.new(pl)
        self.storage_test.new(cy)
        self.storage_test.new(am)
        self.storage_test.new(rv)
        self.storage_test.save()
        self.storage_test.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists(self.path):
            os.remove(self.path)
        if os.path.exists("original_{}".format(self.path)):
            os.rename("original_{}".format(self.path), self.path)
