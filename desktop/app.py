from PIL import Image, ImageQt, ImageDraw
from PyQt6.QtGui import QIcon, QImage, QPixmap
from PyQt6.QtCore import QDir
from desktop.ui_window import Ui_BearFinder
from PyQt6.QtWidgets import QErrorMessage, QMainWindow, QFileDialog
from desktop.PreviewFileDialog import QFileDialogPreview
import os.path
import os


class BearFinderApp(QMainWindow, Ui_BearFinder):
    def __init__(self, find_function):
        print("Ffff")
        super().__init__()
        super().setupUi(self)
        print("FF")
        self.find_function = find_function
        self.info_data = {
            "tilte": "Discription",
            "count": 0,
            "size": (0, 0),
            "dir": "~/",
        }
        self.initUi()
        print("F")
        self.filename = None
        self.work_directory = "~/"
    
    def set_image(self):
        try:
            image = self.find_function(self.filename)
            self.canvas.setPixmap(QPixmap.fromImage(ImageQt(image)))
            self.canvas.update()
        except Exception as err:
            print(err)
            QErrorMessage("Someting went wrong")
        pass

    def run_finder(self):
        # TODO
        pass
    
    def initUi(self):
        self.actionQuit.triggered.connect(self.close)
        self.scrollArea.setWidget(self.canvas)
        self.actionOpen.triggered.connect(self.openAskFileDialog)
        self.setWindowIcon(QIcon("desktop/src/icon.svg"))
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
        Count bears: {self.info_data['count']}
        Image size:  {self.info_data['size']}
        Folder:      {self.info_data['dir']}
        """
    
    def openAskFileDialog(self):
        filedialog = QFileDialogPreview(self,
            "Open File", 
            QDir.currentPath(),
            "Image Files (*.png *.jpg *.jpeg)"
        )
        filedialog.setFileMode(QFileDialog.ExistingFile)
        if filedialog.exec_() == QFileDialogPreview.Accepted:
            self.filename = filedialog.getFileSelected()
            self.work_directory = os.path.dirname(self.filename)
            self.set_image()
