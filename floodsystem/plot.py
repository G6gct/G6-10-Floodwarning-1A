import datafetcher as df
import matplotlib.pyplot as plt
import datetime
import numpy as np
from matplotlib import dates as dat

def plot_water_levels(stations, dt):

    for station in stations:
        dates, levels = df.fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

        # Plot
        plt.plot(dates, levels, label='current levels')
        plt.axhline(y=station.typical_range[0], color='b', linestyle='-', label='typical low levels')
        plt.axhline(y=station.typical_range[1], color='r', linestyle='-', label='typical high levels')

        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45)
        plt.title(station.name)

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels

        plt.legend()

        plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    "plot the best-fit polynomial of p degrees for one station's water level vs. date graph"
    plt.plot(dates, levels, '.')

    poly = polyfit(dates, levels, p)

    # Plot polynomial fit at 50 points along interval
    ndate = dat.date2num(dates)
    shift = np.linspace(ndate[0], ndate[-1], 50)
    plt.plot(shift, poly(shift - shift[0]))
    funct = list(poly(shift - shift[0]))
    ymax = max(poly(shift - shift[0]))
    xpos = funct.index(ymax)
    xmax = shift[xpos]
    plt.annotate('max={}'.format(ymax), xy=(xmax, ymax), xytext=(xmax, ymax),
        arrowprops=dict(facecolor='black', shrink=0.01),
        )
    ymin = min(poly(shift - shift[0]))
    xpos1 = funct.index(ymin)
    xmin = shift[xpos1]
    plt.annotate('min={}'.format(ymin), xy=(xmin, ymin), xytext=(xmin, ymin),
        arrowprops=dict(facecolor='black', shrink=0.01),
        )
    
    plt.title(label='Best-fit polynomial for {}'.format(station))

    # Display plot
    plt.show()
