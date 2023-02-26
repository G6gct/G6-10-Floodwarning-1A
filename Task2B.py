#started
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    stations = build_station_list()
    update_water_levels(stations)

    stations_over_the_threshold = stations_level_over_threshold(stations, 0.8)
    for station in stations_over_the_threshold:
        print (station[0].name, station[1])

if __name__ == "__main__":
    run()