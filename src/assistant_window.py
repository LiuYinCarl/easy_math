# 写一个生成静态HTML页面的程序即可
from PyQt5.QtWidgets import *


class AssistantWindow(QWidget):
    """
    使用助手窗口
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
