# linear algebra
import numpy as np
# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd 
# load csv file based on the python file path
import os
# library used to plot
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
# one-dimensional labeled array
from pandas import Series
# additional module to draw the map
from mpl_toolkits.basemap import Basemap
# hide warnings about depricated dependencies
import warnings
warnings.filterwarnings('ignore')

def show_histograms_by_latitude():
    """
    Displays a histogram that show the amount of
    volcanic eruptions and earthquakes related to the latitude.

    Args:
        none

    Examples:
        
        >>> show_histograms_by_latitude()

    """
    # Read the CSV Files, Eruption.csv and Earthquake.csv
    # Use Pandas read_csv to load the data into a DataFrame,
    # which is far more usable in terms of filtering than my custom
    # function from "Semesterarbeit 1b"
    volcanoes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Eruption.csv'))
    earthquakes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Earthquake.csv'))

    # Filter for occurances newer than 1964
    volcanoes = volcanoes[(volcanoes["Last Known Eruption"]>='1965 CE') & 
                            (volcanoes["Last Known Eruption"]<='2018 CE') &
                            (~volcanoes["Last Known Eruption"].str.contains("BCE")) &
                            (~volcanoes["Last Known Eruption"].str.contains("200 CE"))]

    # the earthquakes dataset has nuclear explosions data in it so 
    # filter these out
    earthquakes_eq=pd.DataFrame()
    earthquakes_eq=earthquakes[earthquakes['Type']=='Earthquake']


    # Get the latitude out of the list of volcanic eruption
    vol_lat = volcanoes["Latitude"].tolist()

    # Get the latitude out of the list of earthquakes
    eq_lat = earthquakes_eq['Latitude'].tolist()

    # Define the size of the figure
    plt.figure(figsize=(15,5))

    # Create the first Histogram with Earthquake data
    plt.subplot(1,2,1) # Define that this should be on top
    plt.hist(eq_lat,bins=100) # Define the "resolution"
    
    # Set axis descriptions and title
    plt.ylabel("Count") 
    plt.xlabel("Latitude in degree")
    plt.title("Earthquake spread by Latitude")

    # Create the second Histogram with Volcanic areas data
    plt.subplot(1,2,2) # Define that this should be on the bottom
    plt.hist(vol_lat,bins=100) # Define the "resolution"

    # Set axis descriptions and title
    plt.ylabel("Count")
    plt.xlabel("Latitude in degree")
    plt.title("Volcanic areas spread by Latitude")

    # Shot the plot
    plt.show()