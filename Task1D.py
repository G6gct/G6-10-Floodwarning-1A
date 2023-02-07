from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list


def run():
    '''The names of the stations located on a river'''

    stations = build_station_list()
    print(f"{len(rivers_with_station(stations))} stations,the first ten are {rivers_with_station(stations)[:10]}")
    print("The names of the stations located on River Aire are", stations_by_river(stations)["River Aire"])
    print("The names of the stations located on River Cam are", stations_by_river(stations)["River Cam"])
    print("The names of the stations located on River Thames are", stations_by_river(stations)["River Thames"])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
