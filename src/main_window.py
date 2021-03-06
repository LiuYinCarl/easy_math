import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.tab_window import TabWindow

# 创建主窗口


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
        new_action = QAction(QIcon('../pictures/新建.png'), '新建文件', self)
        new_action.setShortcut('Ctrl + N')

        save_action = QAction(QIcon('../pictures/保存.png'), '保存文件', self)
        save_action.setShortcut('Ctrl + S')

        close_action = QAction(QIcon('../pictures/关闭.png'), '关闭当前文件', self)

        exit_action = QAction(QIcon('../pictures/exit.png'), '退出', self)
        exit_action.setShortcut('Ctrl + Q')

        undo_action = QAction(QIcon('../pictures/undo.png'), '上一步', self)
        undo_action.setShortcut('Ctrl + Z')

        redo_action = QAction(QIcon('../pictures/redo.png'), '下一步', self)
        redo_action.setShortcut('Ctrl + Shift + Z')

        get_operation_help_action = QAction(QIcon('../pictures/help.png'), '帮助', self)

        feedback_action = QAction(QIcon('../pictures/feedback.png'), '反馈')

        offline_action = QAction('离线模式', self)

        # 在线模式下可以从多个学习网站中进行选择
        # 以下为在线模式的子菜单
        sympy_gamma = QAction(QIcon('../pictures/SympyGamma.png'), 'SympyGamma', self)
        # sympy_gamma.triggered.connect(self.sympygamma_trigger)
        symbolab = QAction(QIcon('../pictures/symbolab.png'), 'Symbolab', self)
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
        self.setWindowIcon(QIcon('../pictures/sailboat.png'))
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    sys.exit(app.exec_())