import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):

    def test_create_instance(self):
        """Test creating a new BaseModel instance."""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        # Check id is valid UUID
        UUID(instance.id)

    def test_str_representation(self):
        """Test string representation."""
        instance = BaseModel()
        expected = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected)

    def test_save_method(self):
        """Test save method updates timestamp."""
        instance = BaseModel()
        old_time = instance.updated_at
        time.sleep(0.1)
        instance.save()
        self.assertNotEqual(old_time, instance.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs."""
        data = {
            "id": "test-123",
            "created_at": "2023-01-01T12:00:00.000000",
            "updated_at": "2023-01-01T12:00:00.000000"
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, "test-123")
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
