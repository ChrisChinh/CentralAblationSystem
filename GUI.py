from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon


SCREEN_WIDTH = 850
SCREEN_HEIGHT = 800

class GUI(QTabWidget):
    def __init__(self):
        # Setup parent container
        super(GUI, self).__init__()
        self.setWindowTitle('This is a test')
        self.setGeometry(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setWindowTitle('Nielson Scientific Ablation System')
        self.setWindowIcon(QIcon('images/icon.ico'))


        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.addTab(self.tab1, 'Tab 1')
        self.addTab(self.tab2, 'Tab 2')

        # self.tab1UI()
        # self.tab2UI()