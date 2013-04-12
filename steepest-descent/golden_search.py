"""
Created on Sun Jan 20 20:44:47 2013

@author: adityavipradas
"""

"""Golden Section Search for locating a local minima of a function 
in a specified closed interval"""
"""Function is continuous and unimodal"""

"""import libraries"""
import math
import sympy as sy

def minimizer(y, a, b, e):
    h = sy.Symbol('h')
    ak = a
    bk = b
    iter = 1

    """initialize the ratio"""
    r = (3 - math.sqrt(5))/2.

    """solve"""
    val1 = a + r*(b - a)
    val2 = b - r*(b - a)
    f1 = y.subs(h, val1)
    f2 = y.subs(h, val2)

    while(math.fabs(b - a)>(e/100.)):
    
        """increment the number of iterations"""
        iter = iter + 1
        
        """eliminate the undesired region"""
        if (f1 <= f2):
            b = val2
            val2 = val1
            val1 = a + r*(b - a)
            f2 = f1
            f1 = y.subs(h, val1)
        else:
            a = val1
            val1 = val2
            val2 = b - r*(b - a)
            f1 = f2
            f2 = y.subs(h, val2)
        
    """store the minima value in xstar"""
    if (f1 <= f2):
        xstar = val1
    else:
        xstar = val2
    return xstar
