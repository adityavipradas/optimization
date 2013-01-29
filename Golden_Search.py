"""
Created on Sun Jan 20 20:44:47 2013

@author: adityavipradas
"""

"""Golden Section Search for locating a local minima of a function 
in a specified closed interval"""
"""Function is continuous and unimodal"""

"""import libraries"""
import math
from pylab import*

"""define function"""
"""change the function as per requirement"""
def equation(x):
    y = (2*math.sin(x))-((x**2)/10.)
    return y
    
"""accept inputs"""  
a = float(raw_input("Enter the lower limit of the closed interval: "))
b = float(raw_input("Enter the upper limit of the closed interval: "))
e = float(raw_input("Enter the final interval of uncertainty(%): "))
ak = a
bk = b
iter = 1

"""initialize the ratio"""
r = (3 - math.sqrt(5))/2.

"""solve"""
x1 = a + r*(b - a)
x2 = b - r*(b - a)
f1 = equation(x1)
f2 = equation(x2)
print"\n"
print "iteration \t a \t b"
print iter,"\t %0.5f"% a,"\t %0.5f"% b

while(math.fabs(b - a)>(e/100.)):
    
    """increment the number of iterations"""
    iter = iter + 1
    
    """eliminate the undesired region"""
    if (f1 <= f2):
        b = x2
        x2 = x1
        x1 = a + r*(b - a)
        f2 = f1
        f1 = equation(x1)
        print iter,"\t %0.5f"% a,"\t %0.5f"% b
    else:
        a = x1
        x1 = x2
        x2 = b - r*(b - a)
        f1 = f2
        f2 = equation(x2)
        print iter,"\t %0.5f"% a,"\t %0.5f"% b
        
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
print "Number of iterations = ",iter
plot(x, val)
scatter(xstar, equation(xstar))
xlabel("x")
ylabel("f(x)")
grid()
show()
