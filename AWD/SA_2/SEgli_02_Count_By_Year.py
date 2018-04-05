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

def show_count_by_year():
    """
    Displays a bar chart that shows the amount of
    earthquakes and erruptions per year, since 1965.

    Args:
        none

    Examples:
        
        >>> show_eq_count_by_year()

    """
    # Read the CSV Files, Eruption.csv and Earthquake.csv
    # Use Pandas read_csv to load the data into a DataFrame,
    # which is far more usable in terms of filtering than my custom
    # function from "Semesterarbeit 1b"
    earthquakes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Earthquake.csv'))
    erruptions = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Eruption.csv'))

    # the earthquakes dataset has nuclear explosions data in it so 
    # filter these out
    earthquakes_eq=earthquakes[earthquakes['Type']=='Earthquake']

    # Convert the date objects to datetime objects
    earthquakes_eq['Date'] = pd.to_datetime(earthquakes_eq['Date'])

    # Filter for occurances newer than 1964
    recent_active = erruptions[(erruptions["Last Known Eruption"]>='1965 CE') & 
                                (erruptions["Last Known Eruption"]<='2018 CE') &
                                (~erruptions["Last Known Eruption"].str.contains("BCE")) &
                                (~erruptions["Last Known Eruption"].str.contains("200 CE"))]

    # Get the year out of the list of earthquakes
    earthquakes_eq['year'] = earthquakes_eq['Date'].dt.year

    # Set the size of the figure
    plt.figure(figsize=(8,20))

    # Define that there should be a little space between the two plots,
    # otherwise the x-axis desciption of the first and the title of the second
    # plot would be displayed above each other.
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=.3)

    # Define that the first graph should be on top
    plt.subplot(2,1,1)

    # Count the earthquake years, group and sort
    series=Series(earthquakes_eq['year']).value_counts().sort_index()
    
    # Specify the kind of the plot
    series.plot(kind="bar")

    # Lable the axes, set a title
    plt.ylabel("Count")
    plt.xlabel("Time in years")
    plt.title("Number of earthquakes by year")

    # Define that the second graph should be below the first one
    plt.subplot(2,1,2)

    # Count the erruption years, group and sort
    series=Series(recent_active['Last Known Eruption']).value_counts().sort_index()
    
    # Specify the kind of the plot
    series.plot(kind="bar")

    # Lable the axes, set a title
    plt.ylabel("Count")
    plt.xlabel("Time in years")
    plt.title("Number of eruptions by year")

    # Show the plot
    plt.show()