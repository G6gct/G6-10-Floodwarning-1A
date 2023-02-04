from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


stations = build_station_list()
p = (52.2053, 0.1218)
r = 10
print(f"The stations within 10 km of the Cambridge city centre: \n {stations_within_radius(stations,p,r)}")
