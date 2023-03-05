#!/usr/bin/python3
import unittest
import models
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ The unittest module provides a rich set of tools for
    constructing and running tests"""

    def test_instance(self):
        """ if is instance of FileStorage """
        test1 = FileStorage()
        self.assertIsInstance(test1, FileStorage)

    def test_docstring_mandatory(self):
        """ docstring at the module are necessary and good practice
        Test assert if there is a docstring at the file_storage
        and the class FileStorage
        """
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)

    def test_permissions(self):
        """ test files are with execution, read, write and existence permission
        X_OK Value to include in the mode parameter of access()
        to determine if path can be executed so we passed
        the file_storage path.
        R_OK Value to include in the mode parameter of access() to test
        the readability of path.
        W_OK Value to include in the mode parameter of access() to test
        the drivability of path.
        F_OK Value to pass as the mode parameter of access() to test
        the existence of path.
        """
        self.assertTrue(os.access("models/engine/file_storage.py", os.X_OK))
        self.assertTrue(os.access("models/engine/file_storage.py", os.R_OK))
        self.assertTrue(os.access("models/engine/file_storage.py", os.W_OK))
        self.assertTrue(os.access("models/engine/file_storage.py", os.F_OK))

    def closing(self):
        """ closing the instance """
        del self.test1
