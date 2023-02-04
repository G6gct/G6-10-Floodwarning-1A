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


def stations_within_radius(stations, centre, r):
    within = []
    for station in stations:
        dist = haversine(centre, station.coord)
        if dist <= r:
            within.append(station.name)
    within_sorted = sorted(within)
    return within_sorted


def rivers_with_station(stations):
    rivers = []
    for station in stations:
        rivers.append(station.river)
    return rivers


def stations_by_river(stations):
    d = {}
    for river in rivers_with_station(stations):
        station_names = []
        for station in stations:
            if river == station.river:
                station_names.append(station.name)
        d[river] = sorted(station_names)
    return d
