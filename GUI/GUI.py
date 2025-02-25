from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont, QPixmap
from GUI.ControlFrame import ControlFrame

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 800
HEADER_HEIGHT = 50

class GUI(QWidget):
    def __init__(self):
        # Setup parent container
        super(GUI, self).__init__()
        self.setGeometry(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setWindowTitle('Nielson Scientific Ablation System')
        self.setWindowIcon(QIcon('images/icon.ico'))

        # Show header
        self.header = QWidget()
        self.header.setFixedSize(SCREEN_WIDTH, HEADER_HEIGHT)
        header_layout = QGridLayout(self.header)
        header_layout.setSpacing(0)
        header_layout.setContentsMargins(10, 10, 0, 0)
        self.header.setFont(QFont('Arial', 20))

        icon = QLabel()
        icon.setPixmap(QPixmap('images/Nielson_Logo.png'))
        icon.setScaledContents(True)
        icon.setFixedSize(80, 40)
        header_layout.addWidget(icon, 0, 0)

        title = QLabel('Nielson Scientific Ablation System')
        title.setFont(QFont('Arial', 20))
        header_layout.setColumnStretch(1, 1)
        header_layout.setColumnStretch(2, 0)
        header_layout.addWidget(title, 0, 2)

        version_string = QLabel('Version: 2.8')
        version_string.setStyleSheet('color: white')
        header_layout.addWidget(version_string, 1, 2)

        # Tab structure
        tab_parent = QTabWidget()
        tab_parent.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT - HEADER_HEIGHT)
        tab_parent.addTab(ControlFrame(), 'Control Frame')
        tab_parent.addTab(QWidget(), 'Logging')
        tab_parent.addTab(QWidget(), 'Experiments')
        tab_parent.addTab(QWidget(), 'Settings')
        tab_parent.addTab(QWidget(), 'Help')

        # Final layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.header)
        layout.addWidget(tab_parent)
        self.setLayout(layout)