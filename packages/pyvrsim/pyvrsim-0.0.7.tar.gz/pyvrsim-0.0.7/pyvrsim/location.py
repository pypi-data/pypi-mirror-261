# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - Abdelouahed Ben Mhamed
Email: a.benmhamed@intelligentica.net
Email: abdelouahed.benmhamed@um6p.ma
Website: https://intelligentica.net
"""
from geopy.geocoders import Nominatim
import pandas as pd
import random
import googlemaps
import folium
import polyline
from IPython.display import IFrame


class Location:
    """
    A class for the Location objects
    :param category: The category of the location (values should be in ('Customer', 'Depot'))
    :param coordinates: The decimal latitude and longitude of the location
    """

    def __init__(self, category, coordinates):
        if not isinstance(coordinates, tuple):
            raise TypeError("Invalid 'coordinates' type. 'coordinates' must be a tuple (x, y)")
        if category not in ['Customer', 'Depot']:
            raise ValueError("'category' must be in 'Customer', 'Depot'")
        self.category = [category]
        self.coordinates = [coordinates]

    def __repr__(self):
        return f"{self.__class__.__name__}(\n" \
               f"\tcategory = {self.category},\n" \
               f"\tcoordinates = {self.coordinates}\n)"

    def __add__(self, other):
        """
        Overloaded + operator to combine two Location objects into a Locations object
        :param other: Another Location object
        :return: Locations object containing both Location objects
        """
        from .locations import Locations

        if not isinstance(other, Location):
            raise TypeError("Invalid 'other' type. 'other' must be an instance of Location")

        # Combine the category and coordinates of both Location objects
        combined_category = self.category + other.category
        combined_coordinates = self.coordinates + other.coordinates

        # Create a new Locations object with the combined information
        combined_locations = Locations([Location(cat, coord) for cat, coord in zip(combined_category, combined_coordinates)])
        return combined_locations
