from PyQt5.QtWidgets import *
from src.create_browser import Browser


class OnlineWindow(QWidget):
    """
    在线模式窗口
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.set_online_window()

    def set_online_window(self):
        layout = QHBoxLayout(self)

        tab_widget = QTabWidget(self)
        layout.addWidget(tab_widget)

        page_1 = Browser(self, url='https://zh.numberempire.com/derivativecalculator.php')
        page_2 = Browser(self, url='https://www.sympygamma.com/')
        page_3 = Browser(self, url='https://zs.symbolab.com/solver')
        page_4 = Browser(self, url='https://www.integral-calculator.com/')
        page_5 = Browser(self, url='https://www.wolframalpha.com /')
        #

        tab_widget.addTab(page_1, 'numberempire')
        tab_widget.addTab(page_2, 'Sympy Gamma')
        tab_widget.addTab(page_3, 'Symbolab')
        tab_widget.addTab(page_4, 'Integral Calculate')
        tab_widget.addTab(page_5, 'WolframAlpha')
