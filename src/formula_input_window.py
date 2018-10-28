import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class FormulaInputWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FormulaInputWindow, self).__init__(parent)

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()
        display = QtWidgets.QLineEdit('0')
        display.setFont(QtGui.QFont("Times", 20))
        display.setReadOnly(False)
        display.setAlignment(QtCore.Qt.AlignRight)
        display.setMaxLength(200)
        layout.addWidget(display)

        input_tabs = CalcInputTabWindow()
        layout.addWidget(input_tabs)
        self.setLayout(layout)


class CalcInputTabWindow(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super(CalcInputTabWindow, self).__init__(parent)
        # self.layout = QtWidgets.QHBoxLayout(self)

        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()

        self.addTab(self.tab1, 'Basic')
        self.addTab(self.tab2, 'sin')
        self.addTab(self.tab3, '123')

        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()

    def tab1_ui(self):
        grid = QtWidgets.QGridLayout()

        symbols = [
            'x^2', 'n^x', '√', 'x√', 'log',
            'pi', '∫', 'Σ', 'Π', 'lim',
            '+', '-', '✕', '÷', '='
        ]

        p = 0
        for sym in symbols:
            button = QtWidgets.QPushButton(sym)
            button.setFixedSize(QtCore.QSize(60, 30))
            # button.clicked.connect(self.buttonClicked)
            grid.addWidget(button, p / 5, p % 5)
            p = p + 1
        self.tab1.setLayout(grid)

    def tab2_ui(self):
        pass
    def tab3_ui(self):
        pass

