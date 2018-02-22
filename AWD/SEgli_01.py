# -*- coding: utf-8 -*-
import math
import time

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

def fib_recursion_count(n):
    f = fib_iterative(n+1)
    return 2*f-1
