from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list



def run():
    stations = build_station_list()
    print(f"The top 9 rivers with the most stations: \n {rivers_by_station_number(stations,9)}")
    print(f"The top 20 rivers with the most stations: \n {rivers_by_station_number(stations,20)}")

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()

