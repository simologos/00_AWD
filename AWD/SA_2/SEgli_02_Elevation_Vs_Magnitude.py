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

def show_pie():
    """
    Displays a pie chart to compare the volcano elevation (meters) 
    and the magnitude of earthquakes.

    Args:
        none

    Examples:
        
        >>> show_pie()

    """
    # Read the CSV Files, Eruption.csv and Earthquake.csv
    # Use Pandas read_csv to load the data into a DataFrame,
    # which is far more usable in terms of filtering than my custom
    # function from "Semesterarbeit 1b"
    volcanoes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Eruption.csv'))
    earthquakes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Earthquake.csv'))

    # the earthquakes dataset has nuclear explosions data in it so 
    # filter these out
    earthquakes_eq=earthquakes[earthquakes['Type']=='Earthquake']

    # Only use the eruptions newer than 1964
    volcanoes = volcanoes[(volcanoes["Last Known Eruption"]>='1965 CE') & 
                            (volcanoes["Last Known Eruption"]<='2018 CE') &
                            (~volcanoes["Last Known Eruption"].str.contains("BCE")) &
                            (~volcanoes["Last Known Eruption"].str.contains("200 CE"))]

    # Get the latitude out of the list of 
    plt.figure(figsize=(10,10))
    
    # Define that the first graph should be on top
    plt.subplot(2,1,1)

    # Round up the elevation to the next 10**3 value, group together and sort.
    series=Series(np.around(volcanoes["Elevation (Meters)"], -3)).value_counts().sort_index()    

    # Specify the kind of the plot
    series.plot(kind="pie")

    # Set the title of the diagram  
    plt.title("Elevation in meters (round up)")

    # Define that the second graph should be on the bottom
    plt.subplot(2,1,2)

    # Round up the Magnitude to the next 10**0 value, group together and sort.
    series=Series(np.around(earthquakes_eq["Magnitude"])).value_counts().sort_index()    
    
    # Specify the kind of the plot
    series.plot(kind="pie")

    # Set the title of the diagram
    plt.title("Earthquakes magnitude (round up)")

    # Show the plot
    plt.show()