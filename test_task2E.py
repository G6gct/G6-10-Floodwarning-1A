from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

station_list = []
for station in stations_highest_rel_level(stations, 5):
    station_list.append(station)


def test_2e():
    assert len(station_list) == 5
