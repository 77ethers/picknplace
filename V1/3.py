from placementLocation import Ui_PlacementLocation
from componentList import Ui_ComponentList
import sys
import pprint
from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import csv
import serial
import numpy as np
import threading
from PyQt5.QtCore import Qt
import pandas as pd
from headMove import Motion

class componentDetails():
    tag = 1
    def __init__(self, componentName, x, y, theta, feederNumber):
        self.componentName = componentName
        self.x = x
        self.y = y
        self.theta = theta
        self.feederNumber = feederNumber
        self.srNumber = componentDetails.tag
        componentDetails.tag += 1

    def __str__(self):
        return  "[Sr number: " + str(self.srNumber) + ", Component Name: " + str(self.componentName) + ", X: " + str(self.x) + ", Y: " + str(self.y) + ", Theta:" + str(self.theta) + ", Feeder no.: " + str(self.feederNumber) + "]"

jobfile_array = []
var1 = 100000

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    Capture = []
    
    def run(self):
        self.ThreadActive = True
        self.Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = self.Capture.read()
            (rows, cols) = frame.shape[:2]
            if ret:
                start_point_verticle = (int(cols/2),0)
                end_point_verticle = (int(cols/2), rows)
                start_point_horizontal = (0, int(rows/2))
                end_point_horizontal = (cols, int(rows/2))
                start_point_rectangle = (int(cols/2)-15, int(rows/2)-15)
                end_point_rectangle = (int(cols/2)+15, int(rows/2)+15)
                line = cv2.line(frame, start_point_verticle, end_point_verticle, (215, 120, 0), 1)
                line2 = cv2.line(line, start_point_horizontal, end_point_horizontal, (215, 120, 0), 1)
                rectangle = cv2.rectangle(line2, start_point_rectangle, end_point_rectangle, (215, 120, 0), 1)
                Image = cv2.cvtColor(rectangle, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.Capture.release()
        self.quit()

class SecondPage(Ui_PlacementLocation):
    
    def __init__(self, window):

        super(SecondPage, self).__init__()
        self.setupUi(window)
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.motion = Motion()

        if var1 != 100000:
            print("working")
            self.componentNameLineEdit.setText(jobfile_array[var1][0])
            self.x1Label.setText(jobfile_array[var1][1])
            self.y1Label.setText(jobfile_array[var1][2])
            self.z1Label.setText(jobfile_array[var1][3])
            self.feederComboBox.setCurrentText(str(jobfile_array[var1][4]))

        else:
            print("else")
   
    def ImageUpdateSlot(self, Image):
        self.liveViewLabel.setPixmap(QPixmap.fromImage(Image))
        
    def yplus(self):
        self.count1 = self.count1 + 1
        #self.motion.headMove(0,1,0,0)
        self.y1Label.setText(str(self.count1))
        
    def xplus(self):
        self.count2 = self.count2 + 1
        #self.motion.headMove(1,0,0,0)        
        self.x1Label.setText(str(self.count2))

    def y2plus(self):
        self.count1 = self.count1 + 2
        #self.motion.headMove(0,2,0,0)
        self.y1Label.setText(str(self.count1))

    def x2plus(self):
        self.count2 = self.count2 + 2
        #self.motion.headMove(2,0,0,0)
        self.x1Label.setText(str(self.count2))
   
    def yminus(self): 
        self.count1 = self.count1 - 1
        #self.motion.headMove(0,-1,0,0)
        self.y1Label.setText(str(self.count1))

    def xminus(self):
        self.count2 = self.count2 - 1
        #self.motion.headMove(-1,0,0,0)
        self.x1Label.setText(str(self.count2))

    def y2minus(self):
        self.count1 = self.count1 - 2
        #self.motion.headMove(0,-2,0,0)
        self.y1Label.setText(str(self.count1))

    def x2minus(self):
        self.count2 = self.count2 - 2
        #self.motion.headMove(-2,0,0,0)
        self.x1Label.setText(str(self.count2))

    def thetaPlus(self):
        self.count3 = self.count3 + 1
        #self.motion.headMove(0,0,0,1)
        self.z1Label.setText(str(self.count3))

    def thetaMinus(self):
        self.count3 = self.count3 - 1
        #self.motion.headMove(0,0,0,-1)        
        self.z1Label.setText(str(self.count3))

    def delete(self):
        self.x1Label.setText("")
        self.y1Label.setText("")
        self.z1Label.setText("")
        self.componentNameLineEdit.setText("")

    def saveLocation(self, abc=-1):  
        global var1
        if  var1 <= len(jobfile_array):
            
            jobfile_array[var1][0] = self.componentNameLineEdit.text()
            jobfile_array[var1][1] = self.x1Label.text()
            jobfile_array[var1][2] = self.y1Label.text()
            jobfile_array[var1][3] = self.z1Label.text()
            jobfile_array[var1][4] = self.feederComboBox.currentText() 
            var1 = 100000

        else: 
            component1 = componentDetails(self.componentNameLineEdit.text(), self.x1Label.text(), self.y1Label.text(), self.z1Label.text(), self.feederComboBox.currentText())
            jobfile_array.append([component1.componentName, component1.x, component1.y, component1.theta, component1.feederNumber])
        
        
        for i in range(0, len(jobfile_array)):
            print (jobfile_array[i])
        
    def createNewComponent(self):
        self.x1Label.setText("")
        self.y1Label.setText("")
        self.z1Label.setText("")
        self.componentNameLineEdit.setText("")
        print(self.componentNameLineEdit.text(), self.x1Label.text(), self.y1Label.text(), self.z1Label.text(), self.feederComboBox.currentText())

    def toggle_back(self):
        
        self.Worker1.stop()
        self.ui = FirstPage(MainWindow)
        
    def download_csv(self):
        x = np.asarray(jobfile_array)
        np.savetxt("name.csv", x, delimiter=',', fmt='%s')
        print("file downloaded")

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class FirstPage(Ui_ComponentList):

    def __init__(self, window):
        super(FirstPage, self).__init__()
        
        self.setupUi(window)
        global jobfile_array
        data_array = pd.DataFrame(jobfile_array, columns=['Component Name', 'X', 'Y', 'Theta', 'Feeder No.'])
        self.model = TableModel(data_array)
        self.tableView.setModel(self.model)
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableView.setFont(font)
        self.tableView.doubleClicked.connect(self.doubleClicked_table)
        #print(data_array)
        



    def doubleClicked_table(self):
        index = self.tableView.selectedIndexes()[0]
        global var1 
        var1 = index.row()
        #print(index.row())
        #print(jobfile_array[var1][0])
        self.ui = SecondPage(MainWindow)
        
    '''def show_selection(self):
        index = self.tableView.currentIndex()
        print(index.row())'''

    def openWindow(self):
        self.ui = SecondPage(MainWindow)
        
    def deleteComponent(self):
        index = self.tableView.selectedIndexes()[0]
        print(index.row())
        jobfile_array.pop(index.row())
        print(jobfile_array)
        self.ui = FirstPage(MainWindow)
    
    def download_file(self):
        x = np.asarray(jobfile_array)
        np.savetxt("name.csv", x, delimiter=',', fmt='%s')
        print("file downloaded")

    def createCopy(self):

        index = self.tableView.selectedIndexes()[0]
        print(index.row())
        print(jobfile_array)
        jobfile_array.append(jobfile_array[index.row()])
        self.ui = FirstPage(MainWindow)

    def editComponent(self):
        index = self.tableView.selectedIndexes()[0]
        print(index.row())
        global var1 
        var1 = index.row()
        self.ui = SecondPage(MainWindow)

    #def inStep(self):
     #   i = len(jobfile_array)
      #  self.tableView.index(0, 1)(self, QBrush(Qt.red), QtCore.Qt.BackgroundRole=True)
        #self.tableView.indexAt(0).setAlternatingRowColors(True)
        #self.tableView.setStyleSheet("alternate-background-color: Light green;")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FirstPage(MainWindow)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        