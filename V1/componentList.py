from PyQt5 import QtCore, QtGui, QtWidgets
import serial


class Ui_ComponentList(object):
       
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(92, 53, 102);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topHorizontalLayout = QtWidgets.QHBoxLayout()
        self.topHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.topHorizontalLayout.setSpacing(40)
        self.topHorizontalLayout.setObjectName("topHorizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(092, 53, 102);\n"
"\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.backButton.setObjectName("backButton")
        self.topHorizontalLayout.addWidget(self.backButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topHorizontalLayout.addItem(spacerItem)
        self.jobFileNameLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jobFileNameLabel.sizePolicy().hasHeightForWidth())
        self.jobFileNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.jobFileNameLabel.setFont(font)
        self.jobFileNameLabel.setStyleSheet("QLabel {color: rgb(255, 255, 255);}")
        self.jobFileNameLabel.setObjectName("jobFileNameLabel")
        self.topHorizontalLayout.addWidget(self.jobFileNameLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topHorizontalLayout.addItem(spacerItem1)
        self.topHorizontalLayout.setStretch(0, 1)
        self.topHorizontalLayout.setStretch(1, 6)
        self.topHorizontalLayout.setStretch(2, 7)
        self.topHorizontalLayout.setStretch(3, 6)
        self.verticalLayout.addLayout(self.topHorizontalLayout)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.tableView.setFont(font)
        self.tableView.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(173, 127, 168);")

        self.tableView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(235)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.tableView)
        self.bottomHorizontalLayout = QtWidgets.QHBoxLayout()
        self.bottomHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomHorizontalLayout.setSpacing(10)
        self.bottomHorizontalLayout.setObjectName("bottomHorizontalLayout")
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newButton.sizePolicy().hasHeightForWidth())
        self.newButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.newButton.setFont(font)
        self.newButton.setStyleSheet("QPushButton {\n"
"\n"
"\n"
"    background-color: rgb(157, 0, 183);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.newButton.setObjectName("newButton")
        self.newButton.clicked.connect(self.openWindow)
        self.bottomHorizontalLayout.addWidget(self.newButton)
        self.createCopyButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createCopyButton.sizePolicy().hasHeightForWidth())
        self.createCopyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.createCopyButton.setFont(font)
        self.createCopyButton.setStyleSheet("QPushButton {\n"
"\n"
"\n"
"    background-color: rgb(157, 0, 183);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.createCopyButton.setObjectName("createCopyButton")
        self.createCopyButton.clicked.connect(self.createCopy)
        self.bottomHorizontalLayout.addWidget(self.createCopyButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("QPushButton {\n"
"\n"
"\n"
"    background-color: rgb(157, 0, 183);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.editButton.setObjectName("editButton")
        self.editButton.clicked.connect(self.editComponent)
        self.bottomHorizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("QPushButton {\n"
"\n"
"\n"
"    background-color: rgb(157, 0, 183);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.deleteComponent)
        self.bottomHorizontalLayout.addWidget(self.deleteButton)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("QPushButton {\n"
"\n"
"\n"
"    background-color: rgb(157, 0, 183);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.download_file)
        self.bottomHorizontalLayout.addWidget(self.saveButton)
        self.inStepButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inStepButton.sizePolicy().hasHeightForWidth())
        self.inStepButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.inStepButton.setFont(font)
        self.inStepButton.setStyleSheet("QPushButton {\n"
"\n"
"    background-color: rgb(0, 8, 204);\n"
"\n"
"\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.inStepButton.setObjectName("inStepButton")
        self.bottomHorizontalLayout.addWidget(self.inStepButton)
        self.startJobButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startJobButton.sizePolicy().hasHeightForWidth())
        self.startJobButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.startJobButton.setFont(font)
        self.startJobButton.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(78, 154, 6);\n"
"\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.startJobButton.setObjectName("startJobButton")
        self.bottomHorizontalLayout.addWidget(self.startJobButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(204, 0, 0);\n"
"\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.stopButton.setObjectName("stopButton")
        self.bottomHorizontalLayout.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.bottomHorizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "<-"))
        self.jobFileNameLabel.setText(_translate("MainWindow", "    Job File Name"))
        self.newButton.setText(_translate("MainWindow", "New"))
        self.createCopyButton.setText(_translate("MainWindow", "Create Copy"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.inStepButton.setText(_translate("MainWindow", "In Step"))
        self.startJobButton.setText(_translate("MainWindow", "Start Job"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ComponentList()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
