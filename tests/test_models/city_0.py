#!/usr/bin/python3
"""Test file for City class"""
from models.city import City

city = City()
print("OK" if type(city) is City else "Fail")
