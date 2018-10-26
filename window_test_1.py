import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_main_window()

    def init_main_window(self):
        """
        @brief: 调用各类组件组成主窗口
        :return:
        """
        tab_widget = TabWindow(self)
        self.setCentralWidget(tab_widget)
        self.set_main_window()
        self.show()

    def set_main_window(self):
        """
        @brief: 设置主窗口的属性
        :return:
        """
        new_action = QAction(QIcon('./pictures/新建.png'), '新建文件', self)
        new_action.setShortcut('Ctrl + N')

        save_action = QAction(QIcon('./pictures/保存.png'), '保存文件', self)
        save_action.setShortcut('Ctrl + S')

        close_action = QAction(QIcon('./pictures/关闭.png'), '关闭当前文件', self)

        exit_action = QAction(QIcon('./pictures/exit.png'), '退出', self)
        exit_action.setShortcut('Ctrl + Q')

        undo_action = QAction(QIcon('./pictures/undo.png'), '上一步', self)
        undo_action.setShortcut('Ctrl + Z')

        redo_action = QAction(QIcon('./pictures/redo.png'), '下一步', self)
        redo_action.setShortcut('Ctrl + Shift + Z')

        get_operation_help_action = QAction(QIcon('./pictures/help.png'), '帮助', self)

        feedback_action = QAction(QIcon('./pictures/feedback.png'), '反馈')

        offline_action = QAction('离线模式', self)

        # 在线模式下可以从多个学习网站中进行选择
        # 以下为在线模式的子菜单
        sympy_gamma = QAction(QIcon('./pictures/SympyGamma.png'), 'SympyGamma', self)
        # sympy_gamma.triggered.connect(self.sympygamma_trigger)
        symbolab = QAction(QIcon('./pictures/symbolab.png'), 'Symbolab', self)
        # symbolab.triggered.connect(self.symbolab_trigger)

        # 菜单栏
        menubar = self.menuBar()

        file = menubar.addMenu('文件')
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(close_action)
        file.addAction(exit_action)

        edit = menubar.addMenu('编辑')
        edit.addAction(undo_action)
        edit.addAction(redo_action)

        model = menubar.addMenu('模式')

        online_action = model.addMenu('在线模式')
        online_action.addAction(sympy_gamma)
        online_action.addAction(symbolab)

        model.addAction(offline_action)

        help = menubar.addMenu('帮助')
        help.addAction(get_operation_help_action)
        help.addAction(feedback_action)

        # 状态栏 (暂未使用)
        statusbar = self.statusBar()

        # 工具栏
        file_toolbar = self.addToolBar('文件')
        file_toolbar.addAction(new_action)
        file_toolbar.addAction(save_action)
        file_toolbar.addAction(close_action)
        file_toolbar.addAction(exit_action)

        edit_toolbar = self.addToolBar('编辑')
        edit_toolbar.addAction(undo_action)
        edit_toolbar.addAction(redo_action)

        help_toolbar = self.addToolBar('帮助')
        help_toolbar.addAction(get_operation_help_action)

        # 主窗口参数
        self.setWindowTitle('Easy Math')
        self.setWindowIcon(QIcon('./pictures/sailboat.png'))
        self.resize(1324, 900)
        self.center()

    def center(self):
        """
        @brief: 主窗口显示在屏幕中心
        :return:
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class TabWindow(QWidget):
    """
    @breif: 利用 QTabWidget 形成三个选项卡
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.set_tab_widget()

    def set_tab_widget(self):
        layout = QHBoxLayout(self)

        tab_widget = QTabWidget(self)
        layout.addWidget(tab_widget)

        page_1 = OnlineWindow(self)
        page_2 = OfflineWindow(self)
        page_3 = AssistantWindow(self)

        tab_widget.addTab(page_1, '在线模式')
        tab_widget.addTab(page_2, '离线模式')
        tab_widget.addTab(page_3, '使用助手')


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
        page_5 = Browser(self, url='https://www.wolframalpha.com/')

        tab_widget.addTab(page_1, 'numberempire')
        tab_widget.addTab(page_2, 'Sympy Gamma')
        tab_widget.addTab(page_3, 'Symbolab')
        tab_widget.addTab(page_4, 'Integral Calculate')
        tab_widget.addTab(page_5, 'WolframAlpha')


class OfflineWindow(QWidget):
    """
    离线模式窗口
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)


class AssistantWindow(QWidget):
    """
    使用助手窗口
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)


class Browser(QWidget):
    """
    @brief 生成一个QWebEngineView， 并显示一个网页
    """

    def __init__(self, parent=None, url=None):
        super(QWidget, self).__init__(parent)
        self.url = url
        self.init_ui()
        self.load()

    def init_ui(self):
        self.webView = QWebEngineView()
        layout = QVBoxLayout(self)
        layout.addWidget(self.webView)

    def load(self):
        self.webView.load(QUrl(self.url))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    sys.exit(app.exec_())
