import sys
from PyQt5.QtCore import (QSettings, Qt, QByteArray)
from PyQt5.QtWidgets import (QAction, QApplication, QListWidget,
                             QMainWindow, QSplitter, QTextBrowser)
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from src.create_browser import Browser
from src.plt_window import MatplotlibWidget
from src.functions import get_abs_path
from src.formula_input_window import FormulaInputWindow


class OfflineWindow(QWidget):
    def __init__(self, parent=None):
        super(OfflineWindow, self).__init__(parent)

        self.input_window = FormulaInputWindow()
        html_path = get_abs_path() + '/show_latex_page.html'  # 获取本地html页面的绝对路径
        print(html_path)
        self.formula_browser = Browser(url=html_path)  # 只允许传入本地页面的绝对路径
        self.figure_canvas = MatplotlibWidget()
        self.figure_canvas.mpl.start_static_plot()  # 测试静态图效果

        # 可用排列方案1
        # self.splitter_1 = QSplitter(Qt.Vertical)
        # self.splitter_1.addWidget(self.formula_browser)
        # self.splitter_1.addWidget(self.input_window)
        #
        # self.splitter_2 = QSplitter(Qt.Horizontal)
        # # self.splitter_2.addWidget(self.splitter_1)
        # self.splitter_2.addWidget(self.figure_canvas)
        #
        # # self.splitter_2.setStretchFactor(0, 1)
        # # self.splitter_2.setStretchFactor(1, 2)
        # self.splitter_1.setStretchFactor(0, 1)
        # self.splitter_1.setStretchFactor(1, 2)
        #
        # self.layout = QHBoxLayout(self)
        # self.layout.addWidget(self.splitter_1)
        # self.layout.addWidget(self.splitter_2)

        # 可用排列方案2 更优
        self.splitter_1 = QSplitter(Qt.Vertical)
        self.splitter_1.addWidget(self.formula_browser)
        self.splitter_1.addWidget(self.input_window)

        self.splitter_2 = QSplitter(Qt.Horizontal)
        self.splitter_2.addWidget(self.splitter_1)
        self.splitter_2.addWidget(self.figure_canvas)

        self.splitter_2.setStretchFactor(0, 1)
        self.splitter_2.setStretchFactor(1, 2)
        self.splitter_1.setStretchFactor(0, 1)
        self.splitter_1.setStretchFactor(1, 2)

        self.layout = QHBoxLayout(self)
        # self.layout.addWidget(self.splitter_1)
        self.layout.addWidget(self.splitter_2)

