#!/usr/bin/python3
"""
city module
"""

from .base_model import BaseModel

class City(BaseModel):
    state_id : str = ""
    name : str = ""
