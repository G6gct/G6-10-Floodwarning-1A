from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


stations = build_station_list()
p = (52.2053, 0.1218)

def test_task1B():
    assert stations_by_distance(stations, p)[0][0] == 'Cambridge Jesus Lock'