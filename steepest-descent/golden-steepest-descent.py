# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:23:32 2013

@author: adityavipradas
"""
#steepest descent method

import math
import sympy as sy
import golden_search

#define function to be minimized
def function(var):
    y = var[0]**2 + var[0] * var[1] + 2 * var[1]**2
    return y
    
def gradient(y, slope, guess, e):
    #slope_val holds values of slope at guess value
    slope_val = [slope[0, 0].subs(x1, guess[0]).subs(x2, guess[1]),\
        slope[1, 0].subs(x1, guess[0]).subs(x2, guess[1])]
    #xiter and yiter hold x and y coordinates of guess for plotting
    xiter.append(guess[0])
    yiter.append(guess[1])
    #prev holds guess for comparison
    prev = guess
    #gold holds guess with alpha parameter ready for golden search
    gold = [guess[0] - (h * slope_val[0]), guess[1] - (h * slope_val[1])]
    #alpha is the function in alpha parameter ready to be minimized
    alpha = function(gold)
    #minima holds minimum value of alpha after golden section search
    #minimizer(function, start, end, interval spacing)
    minima = golden_search.minimizer(alpha, 1, 100, e)
    #get new guess value
    guess = [guess[0] - (minima * slope_val[0]), guess[1] - (minima * slope_val[1])]
    #check condition and proceed
    if math.fabs(prev[0] - guess[0]) > e or math.fabs(prev[1] - guess[1]) > e:
        gradient(y, slope, guess, e)
    return guess

#define symbols globally
x1 = sy.Symbol('x1')
x2 = sy.Symbol('x2')
h = sy.Symbol('h')

#lists for plotting
xiter, yiter = [], []

#y holds function to be minimized
y = function([x1, x2])
#slope holds slope of y
slope = sy.Matrix([[y.diff(x1)], [y.diff(x2)]])
#y and slope do not change throughout code execution 

#guess holds minimum value
#gradient(function, slope, initial guess, interval spacing)
guess = gradient(y, slope, [3, 7], 0.001)

print guess