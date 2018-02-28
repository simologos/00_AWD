# -*- coding: utf-8 -*-
import math
import time
import decimal
from decimal import Decimal

"""
Semesterarbeit Teil 1a - Implementation

This file contains all Python functions implemented as part of the "Semesterarbeit Teil 1a"
    Available functions:
    fib(n)                  
        Calculate the Fibonacci sequence recursively 
    fib_formula(n)          
        Calculate the Fibonacci sequence by using a mathematical formula 
    fib_iterative(n)        
        Calculate the Fibonacci sequence using iteration
    fib_recursion_count(n)  
        Calculate the Nr. of function calls used when using fib(n)
    get_best_recursion_runtime(n)
        Measures the runtime taken when calling fib(n)
    get_best_iteration_runtime(n)
        Measures the runtime taken when calling fib_iterative(n)
    get_best_formula_runtime(n)
        Measures the runtime taken when calling fib_formula(n)

    Open work:
    1.  Reduce the amount of duplicated code for the measurement functions by passing the
        algorythm to use as an argument
    2.  Verify proper implementation with unit tests

"""
def fib(n):
    """
    Naive implementation of the Fibonacci equasion.

    Args:
        n (int): Place of the Fibonacci sequence to calculate


    Examples:
        
        >>> print(fib(5))
        5

    """
    if n == 0:
        #n equals 0, just return 0
        return 0
    elif n == 1:
        #n equals 1, just return 1
        return 1
    else:
        #n is at least 2, call fib (lower n accordingly) 
        #sum the result and return it
        return fib(n-1) + fib(n-2)

def fib_formula(n):
    """
    Implementation of the fibonacci sequence
    based on the developed formula.
    For large n, this is the best performing implementation
    I could found.

    Args:
        n (int): Place of the Fibonacci sequence to calculate


    Examples:
        
        >>> print(fib_formula(5))
        5

    """
    #manual tests have proven that about 1/4 of the input parameter value
    #is enough precision. Tested with values up to n = 1'000'000
    prec = int(n/4)
    
    if(prec < 10):
        #for small n, use at least a presicion of 10 decimals
        prec = 10

    #set the evaluated precision
    decimal.getcontext().prec = prec

    #cache the value of sqrt(5), based on the evaluated precision
    #this value will be smaller / larger
    SQ5_d = Decimal.sqrt(Decimal(5))

    #calculate Φ (big PHI), could be done directly, but this
    #increases the readability
    PHI_d = (Decimal(1) + SQ5_d) / Decimal(2)

    #calculate the n-th value of the fibonnaci sequence
    #details on how this formula was developed can be
    #found in the documentation
    return int(((PHI_d**n) / SQ5_d) + Decimal(0.5))

def fib_iterative(n):
    """
    Implementation of the fibonacci sequence
    by iteration from n backwards until n == 0

    Args:
        n (int): Place of the Fibonacci sequence to calculate


    Examples:
        
        >>> print(fib_iterative(5))
        5

    """
    #set a = 0 and b = 1
    a, b = 0, 1

    #loop for as long as n is greater than 0
    while n > 0:

        #set a = b and b = a+b
        a, b = b, a + b

        #decrement n by 1
        n -= 1
    
    #return the value stored in a
    return a

def fib_recursion_count(n):
    """
    Implementation to determine how many times fib(n)
    would be called (fib(n) means the recursive implementation in this file)
    based on the value of n

    Args:
        n (int): Value which would be passed to fib(n)

    Examples:
        
        >>> print(fib_recursion_count(5))
        15

    """
    
    #get the value of the n-th + 1 fibonnaci number
    #using the best performing implementation available
    #in this file
    f = fib_formula(n+1)

    #double it and substract 1. Further information about this
    #formula can be found in the documentation
    return 2*f-1
    
def get_best_recursion_runtime(n):
    """
    Measures the runtime passed for a call to fib(n)
    This implementation calls fib(n) 10 times
    and returns the best value found.
    Unit of the returned value is seconds.

    Args:
        n (int): Value to pass to fib(n)


    Examples:
        
        >>> print(get_best_recursion_runtime(25))
        0.015625

    """
    #prepare a list to store the result of each run
    times = []

    #loop from 0 to 10 Interval: [0,10)
    for i in range(10):
        #cache the current process time
        t_start = time.process_time()
        
        #call fib
        fib(n)

        #cache the current process time
        t_end = time.process_time()

        #supstract the "starttime" from the "endtime"
        #and store the result in the list.
        times.append(t_end - t_start)

    #return the lowest value because in theorie,
    #the lowest value is reached with minimal interaction
    #from other processes
    return min(times)

def get_best_iteration_runtime(n):
    """
    Measures the runtime passed for a call to fib_iterative(n)
    This implementation calls fib_iterative(n) 10 times
    and returns the best value found.
    Unit of the returned value is seconds.

    Args:
        n (int): Value to pass to fib_iterative(n)


    Examples:
        
        >>> print(get_best_iteration_runtime(25))
        0.0

    """
     #prepare a list to store the result of each run
    times = []

    #loop from 0 to 10 Interval: [0,10)
    for i in range(10):
        #cache the current process time
        t_start = time.process_time()
        
        #call fib_iterative
        fib_iterative(n)

        #cache the current process time
        t_end = time.process_time()

        #supstract the "starttime" from the "endtime"
        #and store the result in the list.
        times.append(t_end - t_start)

    #return the lowest value because in theorie,
    #the lowest value is reached with minimal interaction
    #from other processes
    return min(times)

def get_best_formula_runtime(n):
    """
    Measures the runtime passed for a call to fib_formula(n)
    This implementation calls fib_formula(n) 10 times
    and returns the best value found.
    Unit of the returned value is seconds.

    Args:
        n (int): Value to pass to fib_formula(n)


    Examples:
        
        >>> print(get_best_formula_runtime(25))
        0.0

    """
     #prepare a list to store the result of each run
    times = []

    #loop from 0 to 10 Interval: [0,10)
    for i in range(10):
        #cache the current process time
        t_start = time.process_time()
        
        #call fib_formula
        fib_formula(n)

        #cache the current process time
        t_end = time.process_time()

        #supstract the "starttime" from the "endtime"
        #and store the result in the list.
        times.append(t_end - t_start)

    #return the lowest value because in theorie,
    #the lowest value is reached with minimal interaction
    #from other processes
    return min(times)
