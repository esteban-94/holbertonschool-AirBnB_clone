"""
    Module to testing base_model
"""


from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """ Testing  initialization """

    def test_init(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        self.assertEqual(my_model.name, "My First Model")