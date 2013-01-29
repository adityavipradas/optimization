"""import libraries"""
from __future__ import division
import math
from pylab import*

"""
Created on Sun Jan 20 01:42:50 2013

@author: adityavipradas
"""

"""Fibonacci Search Method for locating a local minima of a function 
in a specified closed interval"""
"""Function is continuous and unimodal"""

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

"""initial length"""
L = []
L.append((b - a))

"""build the fibonacci series"""
F = []
term0 = 0
F.append(term0)
term1 = 1
F.append(term1)
f = term0 + term1
F.append(f)
while (f < (1/(e/100.))):
    term0 = term1
    term1 = f
    f = term0 + term1
    F.append(f)
print"\n"
print "Required fibonacci series is: " 
print F

"""number of iterations required"""
N = len(F) - 1
print"\n"
print "Number of iterations required = ",N-1

"""solve"""
x1 = a + (F[N-2]/F[N])*L[0]
x2 = b - (F[N-2]/F[N])*L[0]
f1 = equation(x1)
f2 = equation(x2)
print"\n"
print "iteration \t a \t b"
print 1,"\t %0.5f"% a,"\t %0.5f"% b
for i in range(2,N):
    L.append((F[N-(i-1)]/F[N])*L[0])
    if (f1 <= f2):
        b = x2
        x2 = x1
        x1 = a + ((F[N-(i+1)]/F[N-(i-1)])*L[i-1])
        f2 = f1
        f1 = equation(x1)
        print i,"\t %0.5f"% a,"\t %0.5f"% b
    else:
        a = x1
        x1 = x2
        x2 = b - ((F[N-(i+1)]/F[N-(i-1)])*L[i-1])       
        f1 = f2
        f2 = equation(x2)
        print i,"\t %0.5f"% a,"\t %0.5f"% b

"""store the minima value in xstar"""
if (f1 <= f2):
    xstar = x1
else:
    xstar = x2

"""plot"""    
x = []
val = []
for i in frange(ak, bk, 0.01):
    x.append(i)
    val.append(equation(i))
print "\n"
print "Minimum value is at x = ", xstar,"\n", "Function value at x is y = ",equation(xstar)
plot(x, val)
scatter(xstar, equation(xstar))
title('Local minima in a function')
xlabel("x")
ylabel("f(x)")
grid()
show()

