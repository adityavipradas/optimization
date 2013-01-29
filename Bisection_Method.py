"""
Created on Sun Jan 20 00:43:19 2013

@author: adityavipradas
"""

"""Bisection Method for locating a local minima of a function in a specified closed interval
Function in the closed interval is continuous and unimodal"""

"""import libraries"""
import math
from pylab import*

"""define function"""
"""change the function as per requirement"""
def equation(x):
    y = (x-1)*(x-2)*(x-3)
    return y

"""accept inputs"""  
a = float(raw_input("Enter the lower limit of the closed interval: "))
b = float(raw_input("Enter the upper limit of the closed interval: "))
e = float(raw_input("Enter the final interval of uncertainty(%): "))
ak = a
bk = b
iter = 0

"""solve"""
while (math.fabs(b - a)>(e/100.)):
    
    """increment the iteration count"""
    iter = iter + 1

    """calculate the values of new points x1 and x2"""
    x1 = ((a + b)/2.) - ((b - a)/4)
    x2 = ((a + b)/2.) + ((b - a)/4)

    """evaluate the values of function at x1 and x2"""
    f1 = equation(x1)
    f2 = equation(x2)
    
    """eliminate the undesired region"""
    if (f1 < f2):
        b = x2
    elif (f2 < f1):
        a = x1

"""store the minima value in xstar"""
if (f1 < f2):
    xstar = x1
else:
    xstar = x2

"""plot"""    
x = []
val = []
for i in frange(ak, bk, 0.01):
    x.append(i)
    val.append(equation(i))
print "Minimum value is at x = ", xstar,"\n", "Function value is y = ",equation(xstar)
print "Number of iterations = ",iter
plot(x, val)
scatter(xstar, equation(xstar))
title('Local minima in a function')
xlabel("x")
ylabel("f(x)")
grid()
show()
