# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
def stations_by_distance(stations, p):
    list = []  
    for station in stations:
        dist = haversine(p, station.coord)
        tuple = (station.name, station.town, dist)
        list.append(tuple)
    list = sorted_by_key(list, 2, reverse=False)
    return list