# 如果要是tab widget中的小部件占据 tab widget的全部大小，需要这样写
# https://stackoverflow.com/questions/35399841/pyqt5-can-qtabwidget-content-extend-up-to-main-window-edges-even-with-no-cont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window With Tabs")
        self.setGeometry(50,50,400,400)

        layout = QVBoxLayout(self) # 要保证有一个self放在里面
        # self.layout = QVBoxLayout() 的写法是错误的

        oTabWidget = QTabWidget(self)
        layout.addWidget(oTabWidget)

# 解决将tabwidget嵌入QMainWindow的问题
# https://pythonspot.com/pyqt5-tabs/
