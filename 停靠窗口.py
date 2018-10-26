import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Dock(QMainWindow):
    def __init__(self):
        super(Dock, self).__init__()
        layout = QHBoxLayout()
        self.dock = QDockWidget('button', self)
        self.bt = QPushButton('push')
        self.dock.setWidget(self.bt)
        self.tt = QTextEdit()
        layout.addWidget(self.tt)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Dock()
    demo.show()
    sys.exit(app.exec_())