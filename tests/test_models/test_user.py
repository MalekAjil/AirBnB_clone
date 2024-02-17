#!/usr/bin/python3
""" User Testing"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Class for User testing"""

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_lastname(self):
        """ Testing for the Lastname"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)
        
    def test_firstname(self):
        """ Testing for the Firstname """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_email(self):
        """ Testing for the User Email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Testing for the user PAssword"""
        new = self.value()
        self.assertEqual(type(new.password), str)