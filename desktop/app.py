from PyQt5.QtGui import QIcon
from desktop.ui_window import Ui_BearFinder
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from desktop.PreviewFileDialog import QFileDialogPreview


class BearFinderApp(QMainWindow, Ui_BearFinder):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.info_data = {
            "tilte": "Discription",
            "count": 0,
            "size": (0, 0),
            "dir": "~/",
        }
        self.initUi()
        self.filename = None
        self.work_directory = "~/"
    
    def initUi(self):
        self.actionOpen.triggered.connect(self.openAskFileDialog)
        self.setWindowIcon(QIcon("desktop/src/icon.svg"))
        toggle_action = self.dockWidget.toggleViewAction()
        toggle_action.setText("toggle info panel")
        self.menuView.addAction(toggle_action)
        self.infoText.setText(self.getInfoText())
    
    def getInfoText(self):
        return f"""
        {self.info_data["tilte"]} 
        Count bears: {self.info_data['count']}
        Image size:  {self.info_data['size']}
        Folder:      {self.info_data['dir']}
        """
    
    def openAskFileDialog(self):
        filedialog = QFileDialogPreview(self,"Open File",
        "","Image Files (*.png *.jpg *.jpeg)")
        filedialog.setFileMode(QFileDialog.ExistingFile)
        if filedialog.exec_() == QFileDialogPreview.Accepted:
            print(filedialog.getFileSelected())


