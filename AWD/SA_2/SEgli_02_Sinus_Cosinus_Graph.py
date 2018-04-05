import matplotlib.pyplot as plt
import numpy as np

def show_sin_cos_graph():
    """
    Displays a graph that shows the sinus and consinus function plot.

    Args:
        none


    Examples:
        
        >>> show_sin_cos_graph()

    """
  # X-Axis
    # Generate 10'000 numbers between 0 and 50
    # Documentation: https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linspace.html
    x = np.linspace(start=0,stop=50,num=10000) # 10'000 linearly spaced numbers

    # Y-Axis
    # y stores the results of the sinus function when adding the x-values
    # Documentation: https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.sin.html
    y_sin = np.sin(x)

    # y_cos stores the results of the consinus function when adding the x-values
    y_cos = np.cos(x)

    # Create the figure
    fig = plt.figure()

    # Set a title
    fig.suptitle('Sinus and Cosinus curve')

    # Describe the axis
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')

    # Draw the functions
    plt.plot(x,y_sin, label="Sinus") # Sinus curve
    plt.plot(x,y_cos, label="Cosinus") # Cosinus curve

    # Show the legend
    legend = plt.legend(loc=1, shadow=True)

    # Show the image
    plt.show()