#!/usr/bin/python3
"""Test file for Place class"""
from models.place import Place

place = Place()
print("OK" if type(place) is Place else "Fail")
