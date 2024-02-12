#!/usr/bin/python3
"""TestBaseModel model"""
import unitest
from models.base_model import BaseModel


class TestBaseModel(unitest.TestCase):
    """Tests BaseModel"""
    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
