import numpy as np
import math as m

a = 0.5
b = 0.9
h = 0.05
d = 0.001

def nfactorial(n):
    return m.factorial(n)  

def pfactorial(n):
    return m.factorial(2*n) * (2*n + 1)

def sum(x, d):
    n = 1
    sum = 0
    term = 1  
    while abs(term) > d:
        term = nfactorial(2*n - 1) / pfactorial(n)  
        sum += term
        n += 1
    return x + sum

xval = np.arange(a, b + h, h)

for x in xval:
    y = sum(x, d)
    print(f"x = {x:.2f}, f(x) = {y:.5f}")
