#!/usr/bin/python3
"""
Testing the amenitys part of the program
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    A sub_class that inherit from
    the class test_basemodel
    """

    def __init__(self, *args, **kwargs):
        """
        test initialiation
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_value(self):
        """
        Testing the value output
        """
        new = self.value()
        self.assertEqual(type(new.name), str)