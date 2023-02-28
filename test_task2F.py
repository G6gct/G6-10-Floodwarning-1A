from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_latest_water_level_data
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.flood import top_water_level

#Get the top stations
station1 = top_water_level(5)[0]
station2 = top_water_level(5)[1]
station3 = top_water_level(5)[2]
station4 = top_water_level(5)[3]
station5 = top_water_level(5)[4]
allstations = [station1, station2, station3, station4, station5]

def test_2f():
    assert len(allstations) == 5
