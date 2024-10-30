import numpy as np  
import math as m    

a = 0.5 
b = 0.9 
h = 0.05 
d = 0.001 

def sum(x, d):
    n = 1      
    total = 0  
    term = 1   
    while abs(term) > d:
        term = m.factorial(2*n - 1) / (m.factorial(2*n) * (2*n + 1))
        total += term  
        n += 1         
    return x + total  

x=0.5
while round(x, 2) <= 0.9:
    y = sum(x, d)
    result= round(y, 2)
    print(f"x = {x:.2f}, f(x) = {result:.5f}") 
    x += 0.05 