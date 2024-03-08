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
from itertools import combinations


class Locations:
    """
    A class for a collection of Location objects
    """

    def __init__(self, locations=None):
        """
        :param locations: Optional list of Location objects to initialize the collection
        """
        self.locations = []
        self.categories = []
        self.coordinates = []
        if locations:
            for location in locations:
                self.add_location(location)

            self.categories = [category for sublist in [loc.category for loc in self.locations] for category in sublist]
            self.coordinates = [coordinates for sublist in [loc.coordinates for loc in self.locations] for coordinates
                                in sublist]

    def add_location(self, location):
        """
        Add a Location object to the collection
        :param location: Location object to be added
        """
        from .location import Location

        if not isinstance(location, Location):
            raise TypeError("Invalid 'location' type. 'location' must be an instance of Location")
        self.locations.append(location)

    def __add__(self, other):
        """
        Add a Location object to the collection
        :param location: Location object to be added
        """
        from .location import Location

        if not isinstance(other, Location):
            raise TypeError("Invalid 'location' type. 'location' must be an instance of Location")
        self.locations.append(other)
        return Locations(self.locations)

    def __repr__(self):
        return f"{self.__class__.__name__}(\n" \
               f"\tcoordinates = {self.coordinates},\n" \
               f"\tcategories = {self.categories}\n)"

    def get_combinations(self, ll):
        # Generate all combinations of 2 elements
        all_combinations = combinations(ll, 2)
        valid_combinations = [(a, b) for a, b in all_combinations if a != b]
        return valid_combinations

    def distance_matrix(self, gmaps=True, gmaps_key=None):
        if gmaps and gmaps_key is not None:
            gmaps_client = googlemaps.Client(key=gmaps_key)
            coordinates = self.coordinates
            combs_coords = self.get_combinations(coordinates)
            distances = []
            for c in combs_coords:
                data = gmaps_client.directions(c[0], c[1], mode="driving")
                distances.append(data[0]['legs'][0]['distance']['value'])

            if len(distances) == len(combs_coords):
                results = []
                for i in range(len(combs_coords)):
                    tmp = combs_coords[i], distances[i]
                    results.append(tmp)
            else:
                results = "Distances not generated"
        else:
            results = "No google maps key was provided"

        return results

    @classmethod
    def create_from_file(cls, file_path):
        """
        Create Location objects by importing from an xlsx, csv, or txt file.
        The file should contain three columns: category, x or longitude, and y or latitude.
        :param file_path: Path to the file
        :return: Locations object
        """
        from .location import Location
        data = pd.read_csv(file_path)

        # Dynamically determine column names
        expected_columns = {'category', 'x', 'y'}
        actual_columns = set(data.columns)

        if expected_columns.issubset(actual_columns):
            category_col = 'category'
            longitude_col = 'x'
            latitude_col = 'y'
        elif {'category', 'longitude', 'latitude'}.issubset(actual_columns):
            category_col = 'category'
            longitude_col = 'longitude'
            latitude_col = 'latitude'
        else:
            raise ValueError(
                "Invalid column names. Columns should be: 'category', 'x', 'y' or 'category', 'longitude', 'latitude'.")

        locations = [Location(row[category_col], (row[longitude_col], row[latitude_col])) for _, row in data.iterrows()]
        return cls(locations)

    @classmethod
    def create_random(cls, num_locations, latitude_limits, longitude_limits, first_as_depot=False):
        """
        Generate Location objects by generating random locations within specified latitude and longitude limits.
        Verify if the location is on land.
        :param num_locations: Number of locations to generate
        :param latitude_limits: Tuple (min_latitude, max_latitude)
        :param longitude_limits: Tuple (min_longitude, max_longitude)
        :param first_as_depot: If True, the first location will be assigned the category 'Depot'
        :return: Locations object
        """
        from .location import Location
        locations = []
        geolocator = Nominatim(user_agent="location_verification")
        counter = 1
        while len(locations) < num_locations:
            latitude = random.uniform(*latitude_limits)
            longitude = random.uniform(*longitude_limits)
            if first_as_depot and counter == 1:
                location = Location("Depot", (round(latitude, 3), round(longitude, 3)))
            else:
                location = Location("Customer", (round(latitude, 3), round(longitude, 3)))

            # Verify if the location is on land
            address = geolocator.reverse((latitude, longitude), language='en')
            if "water" not in address.raw['address']:
                counter += 1
                locations.append(location)

        return cls(locations)
