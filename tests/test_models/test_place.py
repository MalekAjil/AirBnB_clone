#!/usr/bin/python3
""" Testing the Places avaliable"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Class Init"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_cityid(self):
        """ Testing the City ID"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_userid(self):
        """ Testing the User ID"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Testing the city name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Testing the description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_numberRooms(self):
        """ Testing the number of rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_numberBathrooms(self):
        """ Testing the number bath rooms avaliable"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_maxguest(self):
        """ Testing the maxiunm number of Guest """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price(self):
        """ Testing the price"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Testing the location  """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Testing the location  """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenityIds(self):
        """ Testing the amenity_ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)