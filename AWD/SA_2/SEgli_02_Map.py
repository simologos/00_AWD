# linear algebra
import numpy as np
# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd 
# load csv file based on the python file path
import os
# library used to plot
import matplotlib.pyplot as plt
# one-dimensional labeled array
from pandas import Series
# additional module to draw the map
from mpl_toolkits.basemap import Basemap
# hide warnings about depricated dependencies
import warnings
warnings.filterwarnings('ignore')


def print_map():
    """
    Displays a map that shows the location of the earthquakes and the
    volcanic eruptions.

    Args:
        none


    Examples:
        
        >>> print_map()

    """
    # Read the CSV Files, Eruption.csv and Earthquake.csv
    # Use Pandas read_csv to load the data into a DataFrame,
    # which is far more usable in terms of filtering than my custom
    # function from "Semesterarbeit 1b"
    volcanoes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Eruption.csv'))
    earthquakes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Earthquake.csv'))

    # the earthquakes dataset has nuclear explosions data in it so 
    # filter these out
    earthquakes_eq=pd.DataFrame()
    earthquakes_eq=earthquakes[earthquakes['Type']=='Earthquake']

    # Filter for occurances newer than 1964
    volcanoes = volcanoes[(volcanoes["Last Known Eruption"]>='1965 CE') & 
                            (volcanoes["Last Known Eruption"]<='2018 CE') &
                            (~volcanoes["Last Known Eruption"].str.contains("BCE")) &
                            (~volcanoes["Last Known Eruption"].str.contains("200 CE"))]

    # Prepare the map (modified version of the mercator projection, called Miller Cylindrical Projection)
    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners of the map.
    # resolution = 'c' means use crude resolution coastlines.
    baseMap = Basemap(projection='mill',llcrnrlat=-80,urcrnrlat=80, llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
    
    # Prepare the plot to draw the map on
    fig = plt.figure(figsize=(12,10))

    # Get the longitudes out of the list of volcanic eruption
    longitudes_vol = volcanoes["Longitude"].tolist()

    # Get the latitudes out of the list of volcanic eruption
    latitudes_vol = volcanoes["Latitude"].tolist()

    # Get the longitudes out of the list of earthquake
    longitudes_eq = earthquakes_eq["Longitude"].tolist()

    # Get the latitudes out of the list of earthquake
    latitudes_eq = earthquakes_eq["Latitude"].tolist()

    # convert to map projection coords
    x_pt_vol, y_pt_vol = baseMap(longitudes_vol, latitudes_vol)
    x_pt_eq, y_pt_eq = baseMap(longitudes_eq, latitudes_eq)

    # Set the title of the plot
    plt.title("Volcanic areas (red) Earthquakes (blue)")

    # Set the color of the continents
    baseMap.fillcontinents(color='#555555', lake_color='#e0e1e0')

    # Draw the earthquakes and the volcanic areas
    baseMap.plot(x_pt_eq, y_pt_eq, "o", markersize = 3, color = '#007acc')
    baseMap.plot(x_pt_vol, y_pt_vol, "o", markersize = 5, color = '#b2312e')

    # Display the map
    plt.show()