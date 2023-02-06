from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


stations = build_station_list()


def test_c():
    assert stations_by_river(stations)["River Aire"][0] == 'Airmyn'
