# -*- coding: utf-8 -*-
"""
Created on Sun Mai 27 14:45:51 2018

@author: ctsoft
"""
from sympy import Symbol

x = Symbol('x') #define x as sympy symbol
iterate_max = 50 #define maximum amount of iterations
function = x**3+5*x-9 #define function

"""
define function to wrap x_function
to make code more readable
"""
def f(x):
    return eval(str(function))

"""
define newton-raphson method
"""
def bisection(a: float, b: float):
    while b - a > 1e-10:
        m = (a + b) / 2
        if (f(a)* f(m) < 0):
            b = m
        else:
            a = m
    return m
    
# call bisection
print(bisection(-2,2))