import sympy
# 导入可能会用到的符号和数学常量
from sympy import log, E, sqrt, limit


# from sympy import *

# 记录问题
# 问题1：
# 在将字符串中的表达式中的符号（函数，数学常量等）替换为sympy支持的过程中，发现了一个问题，就是如果初始导入的
# 格式为 import sympy  在进行字符串的替换时，如果直接将 log 或者 e(此处以对数符号log和数学常量e为例)替换为sympy.log
# 或者 sympy.E, 会抛出如下错误：
# File "E:\python36\lib\site-packages\sympy\parsing\sympy_parser.py", line 878, in eval_expr
#     code, global_dict, local_dict)  # take local objects in preference
#   File "<string>", line 1, in <module>
# AttributeError: 'Symbol' object has no attribute 'log'
# 具体原因还不清楚
# 解决方案：
#  在导入时直接直接导入需要的常量和符号
# from sympy import log, E
# 然后不要再进行替换即可


def func_name_substitution(string):
    """
    brief: 函数名称代换, 将输入的字符串中的不规范函数名转换为 sympy 中的函数
    :return: 代换过的函数表达式字符串
    """
    # 只要会用到的符号或常量都进行替换，无论替换前后是否相同，保持一致性
    func_dict = {'^': '**', '√': 'sqrt', 'lim': 'limit', '✕': '*', '÷': '/',
                 'e': 'E', 'log': 'log'}
    for key, value in func_dict.items():
        string = string.replace(key, value)
    return string


def converse2latex(convert):
    """
    将sympy 表达式转换为latex
    :return: latex 表达式
    """
    return sympy.latex(convert)


class CalcLimit(object):
    """
    求极限
    """

    def __init__(self, sympy_func, unknowns, limit_point):
        """
        :param sympy_func: sympy 函数表达式
        :param unknowns: 未知数集合
        :param limit_point: 极限点
        """
        self.sympy_func = sympy_func
        self.unknowns = unknowns
        self.limit_point = limit_point

    def calc(self):
        """
        求解极限
        :return: 计算出的极限点的函数值
        """
        return sympy.limit(self.sympy_func, self.unknowns, self.limit_point)


class CalcDerivative(object):
    def __init__(self, func, unknowns, deri_param, times):
        """
        :param func: 函数表达式
        :param unknowns: 未知数列表
        :param deri_param: 求导参数
        :param times: 求导次数
        """
        self.func = func
        self.unknowns = unknowns
        sympy.var(self.unknowns)  # 输入自定义符号
        self.deri_param = deri_param
        self.times = times

    def calc(self):
        """
        求解导数
        :return: 导数计算后的结果
        """
        self.func = func_name_substitution(self.func)
        deri = sympy.Derivative(sympy.sympify(self.func), sympy.S(self.deri_param), self.times).doit()
        return deri

    def get_latex_expr(self, func):
        """
        得到相应sympy表达式的latex表达式
        :param func: sympy 中的函数表达式
        :return: latex 表达式
        """
        return sympy.latex(func)


if __name__ == '__main__':
    # 测试用例

    # 测试含有未知数的表达式
    str_1 = 'x^2 - 6*x + 10'  # 函数表达式
    str_2 = '(1-x)/(1+x)'
    str_3 = 'log((1-x)/(1+x), e)'  # 以10为底
    param = 'x'  # 自变量列表
    deri_param = 'x'  # 求导的自变量
    times = 1  # 求导次数

    demo = CalcDerivative(str_3, param, deri_param, times)
    func = sympy.simplify(demo.calc())
    latex = demo.get_latex_expr(func)

    print(str_3)
    print(func)
    print(latex)
