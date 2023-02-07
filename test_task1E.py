from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list()
def test_rivers_by_station_number():
    list = rivers_by_station_number(stations, 30)
    assert len(list) >= 30





