#!/usr/bin/python3
"""Test file for State class"""
from models.state import State

state = State()
print("OK" if type(state) is State else "Fail")
