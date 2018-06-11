# -*- coding: utf-8 -*-
"""
Created on Sun Mai 27 14:45:51 2018

@author: ctsoft
"""
from sympy import Symbol, diff

x = Symbol('x') #define x as sympy symbol
iterate_max = 50 #define maximum amount of iterations
estimated_root_x = 1 #define the closest x to root
x_function = x**3+5*x-9 #define function
x1_function = diff(x_function, x) #define derivative function

"""
define function to wrap x_function
to make code more readable
"""
def f(x):
    return eval(str(x_function))

"""
define function to wrap x1_function
to make code more readable
"""
def f1(x):
    return eval(str(x1_function))

"""
define newton-raphson method
"""
def newton_iteration(x):
    return x-(f(x)/f1(x))

"""
call newton_iteration as many times as defined in iterate_max
"""
x_calculated = estimated_root_x #initial value

for i in range(0,iterate_max):
    xplus1_calculated = newton_iteration(x_calculated)
    if(x_calculated == xplus1_calculated): #if no more digits can be calculated, stop the iteration
        print('closest approximation of root found and exit iteration')
        break
    else:
        print(xplus1_calculated) #print the calculated approximation
        x_calculated = xplus1_calculated #store the new value