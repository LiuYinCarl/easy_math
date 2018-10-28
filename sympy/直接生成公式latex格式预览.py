# 无效,需要电脑安装latex
from sympy import *

x = symbols('x')
expr = sin(sqrt(x**2 + 20)) + 1
preview(expr, viewer='file', filename='output.png')