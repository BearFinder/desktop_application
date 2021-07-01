from PIL import Image, ImageQt, ImageDraw
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QDir, QThreadPool
from ui_window import Ui_BearFinder
from PyQt6.QtWidgets import QErrorMessage, QMainWindow, QFileDialog, QColorDialog
import os.path

try:
    from detector import init, image_pillow
except ImportError:
    import subprocess
    subprocess.call("bash install.sh")


class BearFinderApp(QMainWindow, Ui_BearFinder):
    def __init__(self, model_name: str):
        super().__init__()
        super().setupUi(self)
        self.find_function = None
        self.image_size = 0, 0,
        self.border_color = "#68e4b2"
        self.detector_acive = False
        self.model_name = model_name
        self.filename = None
        self.work_directory = "~/"
        self.save_filename = None
        self.initUi()
    
    def set_image(self):
        qim = self.run_finder()
        pix = QPixmap.fromImage(qim)
        pix.detach()
        self.canvas.setPixmap(pix)
        self.infoText.setText(self.getInfoText())
    
    def save(self):
        if self.save_filename is None:
            self.save_as()
        self.canvas.pixmap().save(self.save_filename)
    
    def save_as(self):
        self.save_filename = QFileDialog.getSaveFileName(
            self, 'Save As', '', 'All files (*.*);;PNG (*.png);;JPEG(*.jpg)'
        )[0]
        self.save()
                                        

    def run_finder(self):
        image = Image.open(self.filename) 
        self.image_size = image.size
        if not self.detector_acive:
            init(self.model_name)
            self.detector_acive = True
        image = image_pillow(self.filename, color=self.border_color)
        return ImageQt.ImageQt(image)
    
    def initUi(self):
        self.setWindowTitle("Polar Bear finder")

        self.actionSaveAs.triggered.connect(self.save_as)
        self.actionSave.triggered.connect(self.save)
        self.actionQuit.triggered.connect(self.close)
        self.scrollArea.setWidget(self.canvas)
        self.actionOpen.triggered.connect(self.openAskFileDialog)
        self.setWindowIcon(QIcon("src/icon.svg"))
        toggle_action = self.dockWidget.toggleViewAction()
        toggle_action.setText("toggle info panel")
        self.menuView.addAction(toggle_action)
        
        self.colorButton.clicked.connect(self.chooseColor)
        self.infoText.setText(self.getInfoText())
        self.colorButton.setStyleSheet("QWidget { background-color: %s }" % self.border_color)
    
    def chooseColor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.border_color = col.name()
            self.colorButton.setStyleSheet("QWidget { background-color: %s }" % self.border_color)
    
    def getInfoText(self):
        """
        return text to discription panel.
        """
        return f"""Discription\n\nImage:       {self.filename}\n\nFolder:      {self.work_directory}\n\nImage size:  {self.image_size}"""
    
    def openAskFileDialog(self):
        self.filename = QFileDialog.getOpenFileName(self,
            "Open Image", 
            QDir.currentPath(),
            'All files (*.*);;PNG (*.png);;JPEG(*.jpg)'
        )[0]
        self.work_directory = os.path.dirname(self.filename)
        QThreadPool.globalInstance().start(self.set_image)