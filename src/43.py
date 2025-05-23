import sympy as sp

x = sp.Symbol('x')
expr = x**2 - 4*x + 3
solution = sp.solve(expr, x)
print(solution)
