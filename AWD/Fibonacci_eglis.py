# -*- coding: utf-8 -*-
import math
import time
"""Semesterarbeit Teil 1a

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

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
def fib_recursive(n):
    """Implementations.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_formula(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    val = (golden_ratio**n - (1 - golden_ratio)**n) / math.sqrt(5)
    return int(round(val))

def fib_formula_round(n):
    return int(((1 + math.sqrt(5)) / 2) ** n / math.sqrt(5) + 0.5)
    
def fib_matrix(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

print("Measurement start")
elapsed = {}
#elapsed['recursion'] = {}
elapsed['iteration'] = {}
elapsed['formula'] = {}
for i in range(1000):
    """t_start = time.time()
    print(fib_recursive(i))
    t_end = time.time()
    elapsed['recursion'][i] = t_end - t_start
    """
    t_start = time.time()
    #print(fib_iterative(i))
    t_end = time.time()
    elapsed['iteration'][i] = t_end - t_start

    t_start = time.time()
    #print(fib_formula(i))
    t_end = time.time()
    elapsed['formula'][i] = t_end - t_start

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

elapased_ms = pd.DataFrame(elapsed) * 1000
elapased_ms.plot(title='time taken to compute the n-th Fibonaccis number')
plt.ylabel('time taken (ms)')
plt.xlabel('n')
plt.grid(True)
plt.savefig("test.png")
plt.show()
      