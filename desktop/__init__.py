import sys
from desktop.app import BearFinderApp
from PyQt5.QtWidgets import QApplication


def run_application(func):
    app = QApplication(sys.argv)
    ex = BearFinderApp(func)
    ex.show()
    sys.exit(app.exec())