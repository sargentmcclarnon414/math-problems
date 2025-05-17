import numpy as np
from scipy.optimize import fsolve

def f(x):
    return x**2 - 3*x + 1

result = fsolve(f, 2)
print(result)  # Output: 1.0
