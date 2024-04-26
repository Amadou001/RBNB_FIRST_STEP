#!/usr/bin/python3
"""
city module
"""
from .base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id: str = ""
    name: str = ""
