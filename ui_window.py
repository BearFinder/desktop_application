# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BearFinder(object):
    def setupUi(self, BearFinder):
        BearFinder.setObjectName("BearFinder")
        BearFinder.resize(800, 600)
        BearFinder.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(BearFinder)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 641, 531))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.horizontalLayout.addWidget(self.canvas)
        BearFinder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BearFinder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.menuView.setObjectName("menuView")
        BearFinder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BearFinder)
        self.statusbar.setObjectName("statusbar")
        BearFinder.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(BearFinder)
        self.dockWidget.setMinimumSize(QtCore.QSize(120, 174))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoText = QtWidgets.QLabel(self.dockWidgetContents)
        self.infoText.setMaximumSize(QtCore.QSize(300, 16777215))
        self.infoText.setText("")
        self.infoText.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.infoText.setObjectName("infoText")
        self.verticalLayout.addWidget(self.infoText)
        self.colorButton = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.colorButton.sizePolicy().hasHeightForWidth())
        self.colorButton.setSizePolicy(sizePolicy)
        self.colorButton.setMinimumSize(QtCore.QSize(80, 80))
        self.colorButton.setObjectName("colorButton")
        self.verticalLayout.addWidget(self.colorButton)
        self.dockWidget.setWidget(self.dockWidgetContents)
        BearFinder.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionOpen = QtGui.QAction(BearFinder)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpenFolder = QtGui.QAction(BearFinder)
        self.actionOpenFolder.setObjectName("actionOpenFolder")
        self.actionSave = QtGui.QAction(BearFinder)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtGui.QAction(BearFinder)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionQuit = QtGui.QAction(BearFinder)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(BearFinder)
        QtCore.QMetaObject.connectSlotsByName(BearFinder)

    def retranslateUi(self, BearFinder):
        _translate = QtCore.QCoreApplication.translate
        BearFinder.setWindowTitle(_translate("BearFinder", "MainWindow"))
        self.menuFile.setTitle(_translate("BearFinder", "File"))
        self.menuView.setTitle(_translate("BearFinder", "View"))
        self.colorButton.setText(_translate("BearFinder", "Box color"))
        self.actionOpen.setText(_translate("BearFinder", "Open"))
        self.actionOpen.setShortcut(_translate("BearFinder", "Ctrl+O"))
        self.actionOpenFolder.setText(_translate("BearFinder", "Open Folder"))
        self.actionOpenFolder.setShortcut(_translate("BearFinder", "Ctrl+Shift+O"))
        self.actionSave.setText(_translate("BearFinder", "Save"))
        self.actionSave.setShortcut(_translate("BearFinder", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("BearFinder", "Save As"))
        self.actionSaveAs.setShortcut(_translate("BearFinder", "Ctrl+Shift+S"))
        self.actionQuit.setText(_translate("BearFinder", "Quit"))
        self.actionQuit.setShortcut(_translate("BearFinder", "Ctrl+Q"))
