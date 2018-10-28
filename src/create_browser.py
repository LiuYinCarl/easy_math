from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


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
