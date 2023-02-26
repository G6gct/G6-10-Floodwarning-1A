import floodsystem.datafetcher as df
import matplotlib.pyplot as plt
import datetime


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



