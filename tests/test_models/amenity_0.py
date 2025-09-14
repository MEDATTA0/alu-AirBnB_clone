#!/usr/bin/python3
"""Test file for Amenity class"""
from models.amenity import Amenity

amenity = Amenity()
print("OK" if type(amenity) is Amenity else "Fail")
