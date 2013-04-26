from __future__ import division
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:23:32 2013

@author: adityavipradas
"""
#steepest descent method

import math
import sympy as sy
import matplotlib.pyplot as plt
import golden_search

#define function to be minimized
def function(var):
    y = var[0] - var[1] + 2 * var[0]**2 + 2 * var[0] * var[1] + var[1]**2
    return y
    
def gradient(y, slope, guess, e, iter, prev_val):
    iter = iter + 1
    #slope_val holds values of slope at guess value
    slope_val = slope.subs(x1, guess[0]).subs(x2, guess[1])
    print "\n"
    if iter > 1:
        #iteration 2 onwards consists of new direction search
        #find new direction dependent on previous direction
        slope_val = (-1 * slope_val) + ((slope_val.transpose() * slope_val)[0] / \
        (prev_val.transpose() * prev_val)[0]) * (-1 * prev_val)
        slope_val = -1 * slope_val
    #xiter and yiter hold x and y coordinates of guess for plotting
    print slope_val 
    xiter.append(guess[0])
    yiter.append(guess[1])
    #prev holds guess for comparison
    prev = guess
    #gold holds guess with alpha parameter ready for golden search
    gold = [guess[0] - (h * slope_val[0, 0]), guess[1] - (h * slope_val[1, 0])]
    print gold
    #alpha is the function in alpha parameter ready to be minimized
    alpha = function(gold)
    #minima holds minimum value of alpha after golden section search
    #minimizer(function, start, end, interval spacing)
    minima = golden_search.minimizer(alpha, -10, 10, 1)
    print minima
    #get new guess value
    guess = [guess[0] - (minima * slope_val[0, 0]), guess[1] - (minima * slope_val[1, 0])]
    print guess
    print "\n"
    #check condition and proceed
    if math.fabs(prev[0] - guess[0]) > e or math.fabs(prev[1] - guess[1]) > e:
        #store current slope value (slope_val) in prev_val
        gradient(y, slope, guess, e, iter, slope_val)
    res = guess
    return xiter, yiter

#define symbols globally
x1 = sy.Symbol('x1')
x2 = sy.Symbol('x2')
h = sy.Symbol('h')

#lists for plotting
xiter, yiter = [], []

#y holds function to be minimized
y = function([x1, x2])
print y
#slope holds slope of y
slope = sy.Matrix([y.diff(x1), y.diff(x2)])
print slope
#y and slope do not change throughout code execution 

#guess holds minimum value
#gradient(function, slope, initial guess, interval spacing)
xiter, yiter = gradient(y, slope, [1, 1], 0.001, 0, slope)

#plot result
plt.grid()
plt.plot(xiter, yiter)
plt.plot(xiter[-1], yiter[-1],'-o')
plt.legend(["path", "minima"], loc = "best")
plt.annotate((round(xiter[-1], 3), round(yiter[-1], 3)), (xiter[-1], yiter[-1]))
plt.title("conjugate gradient method")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()
