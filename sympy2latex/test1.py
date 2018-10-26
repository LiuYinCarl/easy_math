from sympy import *
import matplotlib.pyplot as plt

a1, a2, a3, a4, a5 = symbols("a1 a2 a3 a4 a5")
f = Function("f")(a1, a2, a3, a4, a5)
g = Function("g")(f)

latex_code = '$' + latex(Derivative(g, a2)) + '$'
print(latex(Derivative(g, a2)))

plt.title(latex_code)
plt.show()


