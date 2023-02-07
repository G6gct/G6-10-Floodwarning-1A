from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation
stations = build_station_list()

def test_incosistent_typical_range_stations():
    list = inconsistent_typical_range_stations(stations)
    counter = 0
    for station in stations:
        if MonitoringStation.typical_range_consistent(station):
            None
        else:
            counter += 1
    print(counter, len(list))
    assert counter == len(list)
