from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
import dateutil

stations = build_station_list()
p = (52.2053, 0.1218)
r = 10


def test_c():
    assert stations_within_radius(stations, p, r)[0] == "Bin Brook"
