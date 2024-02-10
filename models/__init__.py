#!/usr/bin/python3
"""
initialize package instance
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
