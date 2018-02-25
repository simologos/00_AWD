# -*- coding: utf-8 -*-
import math
import time
import decimal
from decimal import Decimal

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
def fib(n):
    """Naive implementation of the Fibonacci equasion.

    Args:
        n (int): Place of the Fibonacci number to calculate


    Examples:
        
        >>> print(fib(5))
        5

    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_formula(n):
    decimal.getcontext().prec = int(n/4)
    SQ5_d = Decimal.sqrt(Decimal(5))
    PHI_d = (Decimal(1) + SQ5_d) / Decimal(2)
    return int(((PHI_d**n)/SQ5_d) + Decimal(0.5))

def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

def fib_recursion_count(n):
    f = fib_iterative(n+1)
    return 2*f-1

    
def get_best_recursion_runtime(n):
    times = []
    for i in range(10):
        t_start = time.process_time()
        fib(n)
        t_end = time.process_time()
        times.append(t_end - t_start)

    return min(times)

def get_best_iteration_runtime(n):
    times = []
    for i in range(10):
        t_start = time.process_time()
        fib_iterative(n)
        t_end = time.process_time()
        times.append(t_end - t_start)

    return min(times)

def get_best_formula_runtime(n):
    times = []
    for i in range(10):
        t_start = time.process_time()
        fib_formula(n)
        t_end = time.process_time()
        times.append(t_end - t_start)

    return min(times)
