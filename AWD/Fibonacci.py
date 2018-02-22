# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:03:59 2018
@author: 1stthomas
"""
import time


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        value = 0
        i0 = 0
        i1 = 1
        for n in range(1, n):
            value = i0 + i1
            i0 = i1
            i1 = value
        return value


def fib1(n):
    """
    Calculates the Fibonacci number of the specified step 'n'.
    Parameters
    ----------
    n : number
      The step of the Fibonacci sequence to be calculated.
    Returns
    -------
    res : number
      The value of the n th step of the Fibonacci.
    Example
    -------
    >>> fib1(10)
    55
    """

    if n == 0 or n == 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


def fibCallsCount(n):
    """
    Calculates the count of function calls to get the Fibonacci number
    of the specified step 'n'.
    Parameters
    ----------
    n : number
      The step of the Fibonacci sequence to be calculated.
    Returns
    -------
    res : number
      The total count of calls of this function.
    Example
    -------
    >>> fibCallsCount(10)
    177
    """

    i = 1
    if n >= 2:
        i1 = fibCallsCount(n - 1)
        i2 = fibCallsCount(n - 2)
        i += i1 + i2

    return i


def fib2(n):
    """
    Calculates the Fibonacci number of the specified step 'n'.
    This method also counts the calls of this method. You can get the count
    by reseting the fib2.count variable to zero, and get its value after
    the execution of this function (see the example).
    Parameters
    ----------
    n : number
      The step of the Fibonacci sequence to be calculated
    Returns
    -------
    res : number
      The value of the n th step of the Fibonacci
    Example
    -------
    >>> fib2.count = 0
    >>> fib2(10)
    55
    >>> fib2.count
    177
    """

    fib2.count += 1
    if n == 0 or n == 1:
        return n
    else:
        return fib2(n - 1) + fib2(n - 2)


def printOutput(f_name, value_type, value):
    """
    Outputs a formated string of the submitted parameters.
    Parameters
    ----------
    f_name : string
      The function name.
    value_type : string
      The type of the value.
    value : mixed
      The value to be printed.
    Example
    -------
    >>> printOutput("fib2(" + str(10) + ")", "value", fib2(10))
    Funktionsaufruf fib2(10) - value: 55
    """

    output = "Funktionsaufruf " + str(f_name) + " - "
    if value_type == "value":
        output += "value: "
    else:
        output += "Anzahl Funktionsaufrufe: "

    output += str(value)

    print(output)


"""
@var step : the step of the fibunacci sequence to be calculated.
"""
step = 55

print("---------------------------")
print("step: " + str(step))
t_start = time.process_time()
printOutput("fib(" + str(step) + ")", "value", fib(step))
t_end = time.process_time()
print("Zeitdifferenz: " + str(t_end - t_start))
print("---------------------------")
print("step: " + str(step))
t_start = time.process_time()
printOutput("fib1(" + str(step) + ")", "value", fib1(step))
t_end = time.process_time()
print("Zeitdifferenz: " + str(t_end - t_start))
print("---------------------------")
fib2.count = 0
printOutput("fib2(" + str(step) + ")", "value", fib2(step))
printOutput("fib2(" + str(step) + ")", "count", fib2.count)
print("---------------------------")
count = fibCallsCount(step)
printOutput("fibCallsCount(" + str(step) + ", 0)", "count", count)