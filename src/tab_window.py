from PyQt5.QtWidgets import *
from src.online_window import OnlineWindow
from src.offline_window import OfflineWindow
from src.assistant_window import AssistantWindow


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
