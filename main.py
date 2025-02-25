import sys
import PySide6.QtWidgets as qt
import PySide6.QtCore as qtc
from GUI.GUI import GUI

if __name__ == '__main__':
    app = qt.QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec())
    