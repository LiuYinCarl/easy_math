import os
import sys

from PyQt5.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout,
    QDesktopWidget, QTextEdit, QLabel, QLineEdit, QPushButton,
    QFileDialog, QProgressBar,
)
from PyQt5.QtCore import QUrl, pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineScript, QWebEnginePage


class Browser(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.webView = QWebEngineView()

        layout = QVBoxLayout(self)
        layout.addWidget(self.webView)

        self.show()
        self.resize(1024, 900)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load(self, url):
        self.webView.load(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = Browser()
    b.load('http://www.bearcarl.top')
    sys.exit(app.exec_())
