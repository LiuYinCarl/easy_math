


# 测试配置未知数符号

# from sympy import *

# var('x, y, z')
# print()


# 测试将sympy 求极限函数转换为latex语句

# from sympy import *
# x = symbols('x')
# expr = S('limit(x**2 - 6*x + 10, x, 2)')
# print(latex(expr, mode='inline'))

# 测试计算嵌套语句

# from sympy import *
# import sympy
# x = sympy.var('x')
# expr = sympy.Derivative((sympy.log((1-x)/(1+x), sympy.E)), x, 1).doit()
# print(sympy.simplify(expr))

# 测试字符串公式

import sympy
# from sympy import log, E
x = sympy.var('x')
expr = 'sympy.log((1-x)/(1+x), E)'
result = sympy.Derivative(sympy.sympify(expr), x, 1).doit()
print(sympy.simplify(result))