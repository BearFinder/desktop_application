import sys
from desktop.app import BearFinderApp
from PyQt5.QtWidgets import QApplication


def run_application():
    app = QApplication(sys.argv)
    ex = BearFinderApp()
    ex.show()
    sys.exit(app.exec())