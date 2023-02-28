from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

stations = build_station_list()

def test_stations_level_over_threshold():
    list = stations_level_over_threshold(stations, 0.6)
    counter = 0
    for station in stations:
        if MonitoringStation.relative_water_level(station) != None and MonitoringStation.relative_water_level(station) > 0.6:
            counter += 1
        else:
            None
    print(counter, len(list))
    
    assert counter == len(list)
