#!/usr/bin/python3
""" 
Testing the base_model 
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ 
    Testing object
    """

    def __init__(self, *args, **kwargs):
        """ 
        initializaiton
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        setup
        """
        pass

    def tearDown(self):
        """Teardown
        """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ 
        Test default
        """
        x = self.value()
        self.assertEqual(type(x), self.value)

    def test_kwargs(self):
        """Test kwargs value
        """
        y = self.value()
        copy_dict = y.to_dict()
        new_dict = BaseModel(**copy_dict)
        self.assertFalse(new_dict is y)

    def test_kwargs_int(self):
        """ 
        test kwargs integer
        """
        v = self.value()
        copy_dict = v.to_dict()
        copy_dict.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy_dict)

    def test_save(self):
        """ 
        Test save
        """
        g = self.value()
        g.save()
        key = self.name + "." + g.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], g.to_dict())

    def test_str(self):
        """
        test strings
        """
        f = self.value()
        self.assertEqual(str(f), '[{}] ({}) {}'.format(self.name, f.id,
                         f.__dict__))

    def test_todict(self):
        """
        test to_dict
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        test kwargs none
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        test kwargs with one
        """
        z = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**z)

    def test_id(self):
        """
        test _id value
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        test _created_at in json
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        test _updated_at in json
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        h = new.to_dict()
        new = BaseModel(**h)
        self.assertFalse(new.created_at == new.updated_at)