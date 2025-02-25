from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont, QPixmap

class ControlFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.tlayout = QGridLayout()
        self.col0 = QVBoxLayout()
        self.col1 = QVBoxLayout()
        self.tlayout.addLayout(self.col0, 0, 0)
        self.tlayout.addLayout(self.col1, 0, 1)
        self.setLayout(self.tlayout)
        self.populate()

    def populate(self):
        pass