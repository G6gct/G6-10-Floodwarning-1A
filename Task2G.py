from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodwarning import floodwarning


def stations_highest_rel_level(stations, N):
    '''
    Takes a list of station objects and integer N.  Returns a list of the N stations (objects) with highest relative water level, sorted in ascending order
    '''
    output_list = [(station, station.relative_water_level()) for station in stations if
                   station.relative_water_level() != None]
    return sorted(output_list, key=lambda x: x[1], reverse=True)[:N]


def run():
    """Requirements for Task 2G"""
    # Create station list
    stations = build_station_list()
    update_water_levels(stations)

    # Reduce the number of stations in the list for demonstration convenience
    demo_stations_tuplelist = stations_highest_rel_level(stations, 10)
    demo_stations = [demo_stations_tuple[0] for demo_stations_tuple in demo_stations_tuplelist]

    # Generate categorized list
    severe_list, high_list, moderate_list, low_list = floodwarning(demo_stations)

    # Print output

    print('')
    print('')
    print('Towns with severe flood risk: ')
    if len(severe_list) == 0:
        print('There is no place with severe flood risk')
        print('')

    else:
        for station_tuple in severe_list:
            station = station_tuple[0]
            risk_factor = station_tuple[1]
            print('')
            print('Station name:', station.town)
            print('Risk factor:', risk_factor)
            print('Latest relative water level:', station.relative_water_level())

    print('')
    print('')
    print('Towns with high flood risk: ')
    if len(high_list) == 0:
        print('There is no place with high flood risk')
        print('')

    else:
        for station_tuple in high_list:
            station = station_tuple[0]
            risk_factor = station_tuple[1]
            print('')
            print('Station name:', station.town)
            print('Risk factor:', risk_factor)
            print('Latest relative water level:', station.relative_water_level())

    print('')
    print('')
    print('Towns with moderate flood risk: ')
    if len(moderate_list) == 0:
        print('There is no place with moderate flood risk')
        print('')

    else:
        for station_tuple in moderate_list:
            station = station_tuple[0]
            risk_factor = station_tuple[1]
            print('')
            print('Station name:', station.town)
            print('Risk factor:', risk_factor)
            print('Latest relative water level:', station.relative_water_level())

    print('')
    print('')
    print('Towns with low flood risk: ')
    if len(low_list) == 0:
        print('There is no place with low flood risk')
        print('')

    else:
        for station_tuple in low_list:
            station = station_tuple[0]
            risk_factor = station_tuple[1]
            print('')
            print('Station name:', station.town)
            print('Risk factor:', risk_factor)
            print('Latest relative water level:', station.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
