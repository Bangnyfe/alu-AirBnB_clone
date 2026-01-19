#!/usr/bin/python3
"""Package initializer for models."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
