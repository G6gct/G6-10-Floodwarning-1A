from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


stations = build_station_list()
update_water_levels(stations)

def test_rivers_by_station_number():
    list = stations_highest_rel_level(stations, 10)
    assert len(list) == 10


