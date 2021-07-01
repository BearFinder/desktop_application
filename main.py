import sys
from PyQt6.QtWidgets import QApplication
from app import BearFinderApp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BearFinderApp()
    ex.show()
    sys.exit(app.exec())