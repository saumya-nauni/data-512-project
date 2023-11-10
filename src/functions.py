import os, json, time
from pyproj import Transformer, Geod
from wildfire.Reader import Reader as WFReader
import geojson
import re

"""

This code example was developed by Dr. David W. McDonald for use in DATA 512,
a course in the UW MS Data Science degree program. This code is provided under the
[Creative Commons](https://creativecommons.org) [CC-BY license](https://creativecommons.org/licenses/by/4.0/).
Revision 1.0 - August 13, 2023

"""

# ---------------------------------------------------------------------------- #
def convert_ring_to_epsg4326(ring_data=None):
    """
    Converts a list of coordinates from ESRI:102008 to EPSG:4326 coordinate system.

    Args:
        ring_data (list of tuples): List of coordinates in ESRI:102008 format.

    Returns:
        list of tuples: List of coordinates converted to EPSG:4326 format.

    Example:
        original_coords = [(x1, y1), (x2, y2), ...]
        converted_coords = convert_ring_to_epsg4326(original_coords)

    Attributions:
        Code Snippet from Dr. David W. McDonald's Notebook
    """
    # initialize an empty list to store the converted coordinates
    converted_ring = []

    # create a transformer to convert from ESRI:102008 to EPSG:4326
    to_epsg4326 = Transformer.from_crs("ESRI:102008", "EPSG:4326")

    # iterate through each coordinate in the ring data and convert it
    for coord in ring_data:
        # transform the coordinate from ESRI:102008 to EPSG:4326
        lat, lon = to_epsg4326.transform(coord[0], coord[1])

        # create a new coordinate tuple in EPSG:4326 format
        new_coord = lat, lon

        # append the new coordinate to the list of converted coordinates
        converted_ring.append(new_coord)

    return converted_ring

# ---------------------------------------------------------------------------- #

def shortest_distance_from_place_to_fire_perimeter(place=None, ring_data=None):
    """
    Calculate the shortest distance from a place to the perimeter of a fire using Haversine formula.

    Args:
        place (tuple): A tuple containing the latitude and longitude of the place in EPSG:4326 format.
        ring_data (list of tuples): List of coordinates representing the fire perimeter in EPSG:4326 format.

    Returns:
        list or None: A list containing the shortest distance in miles and the corresponding coordinates if found.
            Returns None if no closest point is found.

    Example:
        place_coords = (latitude, longitude)
        fire_perimeter = [(lat1, lon1), (lat2, lon2), ...]
        closest_point = shortest_distance_from_place_to_fire_perimeter(place_coords, fire_perimeter)

    Attributions:
        Code Snippet from Dr. David W. McDonald's Notebook
    """
    # convert the ring data to the right coordinate system (EPSG:4326)
    ring = convert_ring_to_epsg4326(ring_data)

    # create a geod object using the WGS84 ellipsoid
    geod = Geod(ellps='WGS84')

    # initialize variables to store the closest point and distance
    closest_point = None
    closest_distance = float('inf')

    # iterate through each point in the converted ring data
    for point in ring:
        # calculate the distance in meters using the Haversine formula
        _, _, distance = geod.inv(place[1], place[0], point[1], point[0])

        # convert the distance to miles
        distance_in_miles = distance * 0.00062137

        # check if the current point is closer than the previously closest point
        if distance_in_miles < closest_distance:
            closest_distance = distance_in_miles
            closest_point = point

    # return the closest point and distance if found, or None if no closest point is found
    if closest_point is not None:
        return [closest_distance, closest_point]
    else:
        return None
