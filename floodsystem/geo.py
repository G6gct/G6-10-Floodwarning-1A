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
    rivers_sorted = sorted(rivers)
    return rivers_sorted


def stations_by_river(stations):
    d = {}
    for river in rivers_with_station(stations):
        station_names = []
        for station in stations:
            if river == station.river:
                station_names.append(station.name)
        d[river] = sorted(station_names)
    return d


def rivers_by_station_number(stations, N):
    dictionary = stations_by_river(stations)
    for river in stations_by_river(stations):
        dictionary[river] = len(dictionary[river])
    tuple = list(dictionary.items())
    tuple.sort(key= lambda x:x[1], reverse=True)
    output = tuple[0:N]
    
    while tuple[N-1][1] == tuple[N][1]:
        output.append(tuple[N])
        N = N+1

    return output





















    