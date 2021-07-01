from PIL import Image, ImageQt, ImageDraw
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QDir
from ui_window import Ui_BearFinder
from PyQt6.QtWidgets import QErrorMessage, QMainWindow, QFileDialog
import os.path


class BearFinderApp(QMainWindow, Ui_BearFinder):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.find_function = None
        self.info_data = {
            "tilte": "Discription",
            "size": (0, 0),
            "dir": "~/",
        }
        self.initUi()
        print("F")
        self.filename = None
        self.work_directory = "~/"
    
    def set_image(self):
        try:
            image = Image.open(self.filename) # TODO: Replace to call detector
            image_qt = ImageQt.ImageQt(image)
            self.canvas.setPixmap(QPixmap.fromImage(image_qt))
            self.canvas.update()
        except Exception as err:
            print(err)
            QErrorMessage("Someting went wrong")
        pass

    def run_finder(self):
        # TODO
        pass
    
    def initUi(self):
        self.setWindowTitle("Polar Bear finder")
        self.actionQuit.triggered.connect(self.close)
        self.scrollArea.setWidget(self.canvas)
        self.actionOpen.triggered.connect(self.openAskFileDialog)
        self.setWindowIcon(QIcon("src/icon.svg"))
        toggle_action = self.dockWidget.toggleViewAction()
        toggle_action.setText("toggle info panel")
        self.menuView.addAction(toggle_action)
        self.infoText.setText(self.getInfoText())
    
    def getInfoText(self):
        """
        return text to discription panel.
        """
        return f"""
        {self.info_data["tilte"]} 
        Image size:  {self.info_data['size']}
        Folder:      {self.info_data['dir']}
        """
    
    def openAskFileDialog(self):
        self.filename = QFileDialog.getOpenFileName(self,
            "Open Image", 
            QDir.currentPath(),
            "Image Files (*.png *.jpg *.jpeg)"
        )[0]
        self.work_directory = os.path.dirname(self.filename)
        self.set_image()