import math as m
import numpy as np

a=3
b=6
h=0.3

xval = np.arange(a, b, h)

for x in xval:
    if x < 4:
        print(f"x={x:.1f}, f(x)={1/(m.sin(1/x)+4):.5f}")
    elif 4 <= x < 5:
        print(f"x={x:.1f}, f(x)={1/(x**2+m.log(x)):.5f}")
    else:
        print(f"x={x:.1f}, f(X)={m.tan((x-3)**3):.5f}")