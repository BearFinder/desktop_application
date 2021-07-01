from PIL import Image, ImageQt, ImageDraw
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QDir, QThreadPool
from ui_window import Ui_BearFinder
from PyQt6.QtWidgets import QErrorMessage, QMainWindow, QFileDialog, QColorDialog
import os.path

try:
    from detector import init, image_pillow
except ImportError:
    pass

class BearFinderApp(QMainWindow, Ui_BearFinder):
    def __init__(self, model_name: str):
        super().__init__()
        super().setupUi(self)
        self.find_function = None
        self.image_size = 0, 0,
        self.border_color = "#AA0000"
        self.detector_acive = False
        self.model_name = model_name
        self.filename = None
        self.work_directory = "~/"
        self.initUi()
    
    def set_image(self):
        im = self.run_finder()
        print(im)
        pix = QPixmap.fromImage(im)
        print("ok")
        self.canvas.setPixmap(pix)
        print("ok")
        self.canvas.update()
        print("u")

    def run_finder(self):
        image = Image.open(self.filename) # TODO: Replace to call detector
        self.image_size = image.size
        if not self.detector_acive:
            init(self.model_name)
            self.detector_acive = True
        image = image_pillow(self.filename, color=self.border_color)
        image.show()
        return ImageQt.ImageQt(image)
    
    def initUi(self):
        self.setWindowTitle("Polar Bear finder")

        self.actionQuit.triggered.connect(self.close)
        self.scrollArea.setWidget(self.canvas)
        self.actionOpen.triggered.connect(self.openAskFileDialog)
        self.setWindowIcon(QIcon("src/icon.svg"))
        toggle_action = self.dockWidget.toggleViewAction()
        toggle_action.setText("toggle info panel")
        self.menuView.addAction(toggle_action)
        
        self.colorButton.clicked.connect(self.chooseColor)
        self.infoText.setText(self.getInfoText())
    
    def chooseColor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.colorButton.setStyleSheet("QWidget { background-color: %s }" % col.name())
            self.border_color = col.name()
    
    def getInfoText(self):
        """
        return text to discription panel.
        """
        return f"""Discription\n\nImage:       {self.filename}\n\nFolder:      {self.work_directory}\n\nImage size:  {self.border_color}"""
    
    def openAskFileDialog(self):
        self.filename = QFileDialog.getOpenFileName(self,
            "Open Image", 
            QDir.currentPath(),
            "Image Files (*.png *.jpg *.jpeg)"
        )[0]
        self.work_directory = os.path.dirname(self.filename)
        QThreadPool.globalInstance().start(self.set_image)