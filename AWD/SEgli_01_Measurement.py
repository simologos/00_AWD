# -*- coding: utf-8 -*-
import math
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from SEgli_01 import *

"""Semesterarbeit Teil 1a

This file contains all Python functions implemented as part of the "Semesterarbeit Teil 1a"

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:

Todo:

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
def show_chart(measurementData):
    figsize(15, 5)
    elapased_ms = pd.DataFrame(measurementData) * 1000
    elapased_ms.plot(title='time taken to compute the n-th Fibonaccis number')
    plt.ylabel('time taken (ms)')
    plt.xlabel('n')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

def show_measurement_recursion(nMmax):
    elapsed = {}
    elapsed['recursion'] = {}
    
    for i in range(nMmax):
        elapsed['recursion'][i] = get_best_recursion_runtime(i)

    show_chart(elapsed)
    return elapsed
    
def show_measurement_formula(nMin, nMmax):
    elapsed = {}
    elapsed['formula'] = {}
    
    for i in range(nMin, nMmax):
        elapsed['formula'][i] = get_best_formula_runtime(i)

    show_chart(elapsed)
    return elapsed

def show_measurement_formula_vs_iterative(nMin, nMmax):
    elapsed = {}
    elapsed['formula'] = {}
    elapsed['iteration'] = {}
    
    for i in range(nMin, nMmax):
        elapsed['formula'][i] = get_best_formula_runtime(i)
        elapsed['iteration'][i] = get_best_iteration_runtime(i)

    show_chart(elapsed)
    return elapsed

def show_measurement_all(nMmax):
    elapsed = {}
    elapsed['recursion'] = {}
    elapsed['iteration'] = {}
    elapsed['formula'] = {}
    
    for i in range(nMmax):
        elapsed['recursion'][i] = get_best_recursion_runtime(i)
        elapsed['iteration'][i] = get_best_iteration_runtime(i)
        elapsed['formula'][i] = get_best_formula_runtime(i)

    show_chart(elapsed)
    return elapsed
