#!/usr/bin/python3
""" Testing the review functionality """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Class Init """

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_placeid(self):
        """ Testing place Id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_userid(self):
        """ Testing User Id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_message(self):
        """ Testing the message """
        new = self.value()
        self.assertEqual(type(new.text), str)