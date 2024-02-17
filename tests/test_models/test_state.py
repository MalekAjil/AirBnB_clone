#!/usr/bin/python3
""" testing the state Functionality """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ TEst Class"""

    def __init__(self, *args, **kwargs):
        """ Init for the steps"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_names(self):
        """Test state names"""
        new = self.value()
        self.assertEqual(type(new.name), str)