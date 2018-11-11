import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class FormulaInputWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FormulaInputWindow, self).__init__(parent)

        self.init_ui()

    def init_ui(self):
        # 主布局
        layout = QtWidgets.QVBoxLayout()
        # 公式输入框
        input_box = QtWidgets.QLineEdit('0')
        input_box.setFont(QtGui.QFont("Times", 20))
        input_box.setReadOnly(False)
        input_box.setAlignment(QtCore.Qt.AlignRight)
        input_box.setMaxLength(200)
        layout.addWidget(input_box)

        # 表单布局
        form_layout = QtWidgets.QFormLayout()
        xyz_label = QtWidgets.QLabel('输入公式中的变量，以空格分开')
        # 自变量输入框
        xyz_box = QtWidgets.QLineEdit()

        form_layout.addRow(xyz_label, xyz_box)
        # 将表单布局添加到主布局中
        layout.addLayout(form_layout)

        # 数学类型选择按钮 子布局
        layout2 = QtWidgets.QHBoxLayout()
        radio_btn_1 = QtWidgets.QRadioButton('导数')
        radio_btn_2 = QtWidgets.QRadioButton('微分')
        radio_btn_3 = QtWidgets.QRadioButton('积分')
        radio_btn_4 = QtWidgets.QRadioButton('极限')
        radio_btn_5 = QtWidgets.QRadioButton('级数')
        radio_btn_6 = QtWidgets.QRadioButton('解方程')

        layout2.addWidget(radio_btn_1)
        layout2.addWidget(radio_btn_2)
        layout2.addWidget(radio_btn_3)
        layout2.addWidget(radio_btn_4)
        layout2.addWidget(radio_btn_5)
        layout2.addWidget(radio_btn_6)

        layout.addLayout(layout2)

        input_tabs = CalcInputTabWindow()
        layout.addWidget(input_tabs)
        self.setLayout(layout)

    def radio_btn_select(self, btn):
        if btn.text() == '导数' and btn.isChecked() == True:
            layout = QtWidgets.QFormLayout
            label = QtWidgets.QLabel('求导次数')
            times_box = QtWidgets.QDateEdit()
            layout.addRow(label, times_box)

        elif btn.text() == '微分' and btn.isChecked() == True:
            pass
        elif btn.text() == '积分' and btn.isChecked() == True:
            pass
        elif btn.text() == '极限' and btn.isChecked() == True:
            pass
        elif btn.text() == '级数' and btn.isChecked() == True:
            pass
        elif btn.text() == '解方程' and btn.isChecked() == True:
            pass


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

    # 基本字符按键板
    def tab1_ui(self):
        """
        基本函数按键板
        """
        grid = QtWidgets.QGridLayout()

        symbols = [
            'x^2', 'n^x', '√', 'x√', 'log',
            'pi', '∫', 'Σ', 'Π', 'lim',
            '+', '-', '✕', '÷', '=',
            '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0'
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
        """
        三角函数按键板
        """
        grid = QtWidgets.QGridLayout()

        symbols = [
            'sin', 'cos', 'tan', 'cot', 'sec',
            'csc', 'arcsin', 'arccos', 'arctan', 'arccot',
            '+', '-', '✕', '÷', '=',
            '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0'
        ]

        p = 0
        for sym in symbols:
            button = QtWidgets.QPushButton(sym)
            button.setFixedSize(QtCore.QSize(60, 30))
            # button.clicked.connect(self.buttonClicked)
            grid.addWidget(button, p / 5, p % 5)
            p = p + 1
        self.tab1.setLayout(grid)

    def tab3_ui(self):
        """
        数字按键板
        :return:
        """
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
