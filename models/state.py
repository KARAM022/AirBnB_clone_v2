#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    ___tablename__ = 'states'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("PlaceAmenity", back_populates="amenity")
