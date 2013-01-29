"""
Created on Sat Jan 19 01:20:02 2013

@author: adityavipradas
"""
"""Two point equal interval search method for finding the local minima within a specified closed interval
Function within the interval being continous and unimodal"""

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
    x1 = a + ((b - a)/3.)
    x2 = b - ((b - a)/3.)
    
    """evaluate the values of function at x1 and x2"""
    f1 = equation(x1)
    f2 = equation(x2)
    
    """eliminate the undesired region"""
    if (f1 < f2):
        b = x2
    elif (f2 < f1):
        a = x1
    else:
        b = x2
        a = x1
        
"""store the minima value in xstar"""
if (f1 < f2):
    xstar = x1
else:
    xstar = x2

"""plot"""    
x = []
val = []
for i in frange(ak, bk, (e/100.)):
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
