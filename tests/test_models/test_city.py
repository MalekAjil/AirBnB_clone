#!/usr/bin/python3
"""
Testing the City model
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """A sub_class that inherit from
    the class test_basemodel """

    def __init__(self, *args, **kwargs):
        """
        test initialiation
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Testing the state id
        """
        value = self.value()
        self.assertEqual(type(value.state_id), str)

    def test_state_name(self):
        """
        Testing the state name
        """
        value = self.value()
        self.assertEqual(type(value.name), str)