#!/usr/bin/python3
"""Simple tests for FileStorage."""
import os
import unittest
import tempfile
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        FileStorage._FileStorage__file_path = self.temp_file.name
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up test fixtures."""
        try:
            os.unlink(self.temp_file.name)
        except:
            pass

    def test_all_returns_dict(self):
        """Test all() returns dictionary."""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object(self):
        """Test new() adds object to storage."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test save() creates JSON file."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists(self.temp_file.name))

    def test_reload_loads_objects(self):
        """Test reload() loads objects from file."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        # Clear objects and reload
        FileStorage._FileStorage__objects = {}
        storage.reload()

        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

    def test_delete_removes_object(self):
        """Test delete() removes object."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.delete(obj)
        key = f"BaseModel.{obj.id}"
        self.assertNotIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
