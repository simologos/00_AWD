import matplotlib.pyplot as plt
import numpy

def show_sin():
    """
    Displays a graph that shows the sinus function plot.

    Args:
        none

    Examples:
        
        >>> show_sin()

    """
    # X-Axis
    # Generate 10'000 numbers between 0 and 50
    # Documentation: https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linspace.html
    x = numpy.linspace(start=0,stop=50,num=10000) # 10'000 linearly spaced numbers

    # Y-Axis
    # y stores the results of the sinus function when adding the x-values
    # Documentation: https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.sin.html
    y = numpy.sin(x)

    # Generate the figure
    fig = plt.figure()

    # Add a title
    fig.suptitle('Sinus curve')

    # Describe the axes
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')

    # Draw the function
    plt.plot(x,y)

    # Show the graph
    plt.show()