from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


stations = build_station_list()
print("The names of the stations located on River Aire are", stations_by_river(stations)["River Aire"])
print("The names of the stations located on River Cam are", stations_by_river(stations)["River Cam"])
print("The names of the stations located on River Thames are", stations_by_river(stations)["River Thames"])
