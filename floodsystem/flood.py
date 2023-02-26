from .utils import sorted_by_key
from .stationdata import build_station_list

def stations_level_over_threshold(stations, tol):
    output = []
    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() > tol:
            output.append(tuple((station, station.relative_water_level())))
    return sorted_by_key(output, 1, True)