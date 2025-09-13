#!/bin/usr/python3
"""
Init for models.engine submodule: sets up storage instance.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
