from sympy import *


x, y, z, t = symbols('x, y, z, t')
k, m, m = symbols('k, m, n', integer=True)
f, g, h = symbols('f, g, h', cls=Function)


s = expand(exp(I*x), complex=True)
print(s)