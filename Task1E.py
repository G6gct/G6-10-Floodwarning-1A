from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from test_stationdata import test_build_station_list

stations = build_station_list()
print(f"The top 9 rivers with the most stations: \n {rivers_by_station_number(stations,9)}")
print(f"The top 20 rivers with the most stations: \n {rivers_by_station_number(stations,20)}")