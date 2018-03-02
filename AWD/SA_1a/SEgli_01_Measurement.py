# -*- coding: utf-8 -*-
import math
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from SEgli_01_Fibonacci import *

"""
Semesterarbeit Teil 1a - Plot runtime analyse using mathplotlib

This file offers a convenient way to display runtime measurement results
by displaying a diagram created with mathplotlib.

This functionallity is implemented in a different file since I am not certain
if the students are allowed to use the mathplotlib for this work.

"""
def show_chart(measurementData):
    """
    Displays a chart based on Argument measurementData.

    Args:
        measurementData (dictionary): The data to plot


    Examples:
        
        >>> show_chart({reursive={1 = 0.0,2=0.1}})

    """
    #set the dimension of the graph
    figsize(15, 5)

    #transform the input of the data from seconds to ms.
    elapased_ms = pd.DataFrame(measurementData) * 1000
    
    #Set the title of the graph
    elapased_ms.plot(title='time taken to compute the n-th Fibonaccis number')
    
    #set the vertical lable text
    plt.ylabel('time taken (ms)')

    #set the horizontal lable text
    plt.xlabel('n')

    #tell mathplotlib to display a grid
    plt.grid(True)

    #Set the name of the file to store the graph into
    plt.savefig("fib_runtime_plot.png")

    #display the graph
    plt.show()

def show_measurement_recursion(nMax):
    """
    Callects data while calling fib(n)
    and calls show_chart().

    After displaying the plot, the function returns the dictionary 
    of collacted data to the callee.

    Args:
        nMax (int): The upper limit of the argument for fib(n)


    Examples:
        
        >>> show_measurement_recursion(5)

    """
    #initialize the dictionary
    elapsed = {}

    #define a key to store the data in
    elapsed['recursion'] = {}
    
    #starting at 0, measure the runtime for each n in interval [0, nMax)
    for i in range(nMax):
        #measure the runtime for n = i
        elapsed['recursion'][i] = get_best_recursion_runtime(i)

    #show the data to the user
    show_chart(elapsed)

    #and also return it
    return elapsed
    
def show_measurement_formula(nMin, nMax):
    """
    Collects data while calling fib_formula(n)
    and calls show_chart().

    After displaying the plot, the function returns the dictionary 
    of collacted data to the callee.

    Args:
        nMin (int): The lower limit of the argument for fib_formula(n)
        nMax (int): The upper limit of the argument for fib_formula(n)


    Examples:
        
        >>> show_measurement_formula(5,10)

    """

    #initialize the dictionary
    elapsed = {}

    #define a key to store the data in
    elapsed['formula'] = {}
    
    #starting at nMin, measure the runtime for each n in interval [nMin, nMax)
    for i in range(nMin, nMax):
        #measure the runtime for n = i
        elapsed['formula'][i] = get_best_formula_runtime(i)

    #show the data to the user
    show_chart(elapsed)

    #and also return it
    return elapsed

def show_measurement_formula_vs_iterative(nMin, nMax):
    """
    Collects data while calling fib_formula(n) and fib_iterative() sequentially
    and calls show_chart().

    After displaying the plot, the function returns the dictionary 
    of collacted data to the callee.

    Args:
        nMin (int): The lower limit of the argument for the fibonacci implementations to call
        nMax (int): The upper limit of the argument for the fibonacci implementations to call


    Examples:
        
        >>> show_measurement_formula_vs_iterative(5,10)

    """
    #initialize the dictionary
    elapsed = {}

    #define keys to store the data in
    elapsed['formula'] = {}
    elapsed['iteration'] = {}

    #starting at nMin, measure the runtime for each n in interval [nMin, nMax)
    for i in range(nMin, nMax):
        #measure the fib_formula runtime for n = i
        elapsed['formula'][i] = get_best_formula_runtime(i)
        #measure the fib_iterative runtime for n = i
        elapsed['iteration'][i] = get_best_iteration_runtime(i)

    #show the data to the user
    show_chart(elapsed)

    #and also return it
    return elapsed

def show_measurement_all(nMax):
    """
    Collects data while calling all available fibonnaci 
    sequence implementations sequentially
    and calls show_chart() once done.

    After displaying the plot, the function returns the dictionary 
    of collacted data to the callee.

    Please note: Because of the heavy impact on the runtime when calling
    fib(n), this function does not have an nMin parameter to start
    measurement with values for n > 0.

    Args:
        nMax (int): The upper limit of the argument for the fibonacci implementations to call


    Examples:
        
        >>> show_measurement_all(10)

    """
    #initialize the dictionary
    elapsed = {}

    #define keys to store the data in
    elapsed['recursion'] = {}
    elapsed['iteration'] = {}
    elapsed['formula'] = {}
    
    #starting at 0, measure the runtime for each n in interval [0, nMax)
    for i in range(nMax):
        #measure the fib(n) runtime for n = i
        elapsed['recursion'][i] = get_best_recursion_runtime(i)
        #measure the fib_iterative(n) runtime for n = i
        elapsed['iteration'][i] = get_best_iteration_runtime(i)
        #measure the fib_formula(n) runtime for n = i
        elapsed['formula'][i] = get_best_formula_runtime(i)

    #show the data to the user
    show_chart(elapsed)

    #and also return it
    return elapsed
