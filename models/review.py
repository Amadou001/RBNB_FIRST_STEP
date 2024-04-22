#!/usr/bin/python3
"""
review module
"""


from .base_model import BaseModel

class Review(BaseModel):
    place_id : str = ""
    user_id : str = ""
    text : str = ""
