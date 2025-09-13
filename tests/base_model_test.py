import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):

    def test_str_representation(self):
        """Test the __str__ method returns the expected format."""
        instance = BaseModel()
        expected = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected)

    def test_init_with_kwargs(self):
        """Test initializing BaseModel with kwargs sets attributes correctly."""
        now = datetime.now().isoformat()
        data = {
            "id": "1234",
            "created_at": now,
            "updated_at": now
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, "1234")
        self.assertEqual(instance.created_at.isoformat(), now)
        self.assertEqual(instance.updated_at.isoformat(), now)

    def test_create_instance(self):
        """Test that a new BaseModel instance is properly initialized."""
        instance = BaseModel()
        # Check type
        self.assertIsInstance(instance, BaseModel,
                              "Object is not a BaseModel instance")
        # Check id is a valid UUID string
        try:
            UUID(instance.id)
        except ValueError:
            self.fail(f"id '{instance.id}' is not a valid UUID")
        self.assertIsInstance(instance.id, str, "id is not a string")
        # Check timestamps
        self.assertIsInstance(instance.created_at, datetime,
                              "created_at is not a datetime object")
        self.assertIsInstance(instance.updated_at, datetime,
                              "updated_at is not a datetime object")
        # created_at and updated_at should be very close
        time_diff = abs(
            (instance.updated_at - instance.created_at).total_seconds())
        self.assertLessEqual(
            time_diff, 1, "updated_at and created_at should be nearly equal on creation")

    def test_save_instance(self):
        instance = BaseModel()
        time_1 = instance.updated_at
        time.sleep(2)
        instance.save()
        time_2 = instance.updated_at
        time_diff = abs((time_1 - time_2).total_seconds())
        self.assertNotEqual(
            time_diff, 2, "the times should be at least 2 seconds apart")

    def test_to_dict(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        created_at = instance_dict.get("created_at")
        updated_at = instance_dict.get("updated_at")
        try:
            datetime.fromisoformat(created_at)
            datetime.fromisoformat(updated_at)
        except:
            self.fail("created_at and/or updated_at are not iso format")


if __name__ == "__main__":
    unittest.main()
