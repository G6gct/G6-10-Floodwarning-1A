from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodwarning import floodwarning


def stations_highest_rel_level(stations, N):
	'''
	Takes a list of station objects and integer N.  Returns a list of the N stations (objects) with highest relative water level, sorted in ascending order
	'''
	output_list = [(station, station.relative_water_level()) for station in stations if station.relative_water_level() != None]
	return sorted(output_list, key=lambda x: x[1], reverse=True)[:N]


def run():
    """Requirements for Task 2G"""
    # Create station list
    stations = build_station_list()
    update_water_levels(stations)

    # Reduce the number of stations in the list for demonstration convenience
    demo_stations_tuplelist = stations_highest_rel_level(stations, 10)

def test_2f():
      assert len(demo_stations_tuplelist) == 10