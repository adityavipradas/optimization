"""import libraries"""
from __future__ import division
import math
from pylab import*
"""
Created on Tue Jan 29 15:19:55 2013

@author: adityavipradas
"""

"""Quadratic Langrangian Interpolation method for finding the local minima within a specified closed interval
Function within the interval being continous and unimodal"""

"""define function"""
"""change the function as per requirement"""
def equation(x):
    y = (x-1)*(x-2)*(x-3)
    return y

def QuadInter(x, a, b, c, fa, fb, fc):
    y = ((fa * (((x - b)*(x - c))/((a - b)*(a - c)))) + (fb * (((x - a)*(x - c))/((b - a)*(b - c)))) + (fc * (((x - a)*(x - b))/((c - a)*(c - b)))))
    return y

"""accept inputs"""  
a = float(raw_input("Enter the lower limit of the closed interval: "))
b = float(raw_input("Enter the upper limit of the closed interval: "))
e = float(raw_input("Enter the final interval of uncertainty(%): "))
iter = 0
ak = a
bk = b

"""obtain the third point on the function"""
c = a + ((b - a)/2)
ck = c

"""calculate the function values"""
fa = equation(a)
fb = equation(b)
fc = equation(c)
fak = fa
fbk = fb
fck = fc

print"\n"
print "iteration \t a \t b"
print iter,"\t %0.5f"% a,"\t %0.5f"% b

while(math.fabs(b - a) > (e/100.)):
    iter = iter + 1
    """find the minima in the interpolated quadratic function"""
    if ((((b - c)*fa) + ((c - a)*fb) + ((a - b)*fc)) != 0):
        x = (1/2)*(((((b**2)-(c**2))*fa) + (((c**2)-(a**2))*fb) + (((a**2)-(b**2))*fc))/(((b - c)*fa) + ((c - a)*fb) + ((a - b)*fc)))
    else:
        print "Change the limits of closed intervals....Division by zero not possible"
        exit()
    fx = equation(x)
    
    """eliminate the undesired region"""
    if ((x < c) and (fx < fc)):
        b = c
        c = x
        fb = fc
        fc = fx
        print iter,"\t %0.5f"% a,"\t %0.5f"% b
    elif ((x < c) and (fx >= fc)):
        a = x
        fa = fx
        print iter,"\t %0.5f"% a,"\t %0.5f"% b
    elif ((x > c) and (fx <= fc)):
        a = c
        c = x
        fa = fc
        fc = fx
        print iter,"\t %0.5f"% a,"\t %0.5f"% b
    else:
        b = x
        fb = fx
        print iter,"\t %0.5f"% a,"\t %0.5f"% b

"""plot"""    
xstar = []
val1 = []
val2 = []
for i in frange(ak, bk, 0.01):
    xstar.append(i)
    val1.append(equation(i))
    val2.append(QuadInter(i, ak, bk, ck, fak, fbk, fck))
print "\n"
print "Minimum value is at x = ", x,"\n", "Function value at x is y = ",equation(x)
print "Number of iterations = ",iter
plot(xstar, val1)
plot(xstar, val2, '--')
xlabel("x")
ylabel("f(x)")
scatter(x, equation(x))
grid()
show()
