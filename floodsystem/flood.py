from .utils import sorted_by_key
from .stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_latest_water_level_data
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def stations_level_over_threshold(stations, tol):
    output = []
    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() > tol:
            output.append(tuple((station, station.relative_water_level())))
    return sorted_by_key(output, 1, True)

def stations_highest_rel_level(stations, N):
    output = []
    for station in stations:
        if station.relative_water_level() != None:
            output.append(tuple((station, station.relative_water_level())))
    output = sorted_by_key(output, 1, True)
    output_final = [ ]
    for n in output:
        output_final.append(n[0])
    return output_final[:N]

#Define a function that finds the top x stations in terms of the water level
def top_water_level(x):
    "Search for the  top x stations with highest water level"
    data = fetch_latest_water_level_data()
    items = data['items']
    rank = []

    #getting the data
    for w in items:
        m = dict(w)
        
        measures = m.get('latestReading')
        if measures != None:
            value = measures['value']
            if type(value) == float:
                rank.append((w["@id"], value, w["label"]))
    
    #sorting the data
    sort = sorted(rank, key=lambda x: x[1], reverse = True)
    return sort[:x]