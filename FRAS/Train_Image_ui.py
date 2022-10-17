from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread



class Ui_Train_Image(object):
    # -------------- image labesl ------------------------

    def getImagesAndLabels(self,path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # print(imagePaths)

        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids


    # ----------- train images function ---------------
    def TrainImages(self):
        
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, Id = self.getImagesAndLabels("TrainingImage")
        Thread(target = recognizer.train(faces, np.array(Id))).start()
        # Below line is optional for a visual counter effect
        Thread(target = self.counter_img("TrainingImage")).start()
        recognizer.save("TrainingImageLabel"+os.sep+"Trainner.yml")
        #self.label.setText(self.text)

    # Optional, adds a counter for images trained (You can remove it)
    def counter_img(self,path):
        imgcounter = 1
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        for imagePath in imagePaths:
            self.text=(str(imgcounter) + " Images Trained")
            #print(self.text)
            time.sleep(0.008)
            imgcounter += 1
            
        self.label.setText(self.text)

    def setupUi(self, Train_Image):
        Train_Image.setObjectName("Train_Image")
        Train_Image.resize(422, 120)
        Train_Image.setMinimumSize(QtCore.QSize(422, 120))
        Train_Image.setMaximumSize(QtCore.QSize(422, 120))
        self.widget = QtWidgets.QWidget(Train_Image)
        self.widget.setGeometry(QtCore.QRect(0, 0, 421, 121))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0.167464 rgba(114, 56, 255, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 10, 301, 41))
        self.label.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget,clicked=lambda:self.TrainImages())
        self.pushButton.setGeometry(QtCore.QRect(130, 83, 141, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 12px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Train_Image)
        QtCore.QMetaObject.connectSlotsByName(Train_Image)

    def retranslateUi(self, Train_Image):
        _translate = QtCore.QCoreApplication.translate
        Train_Image.setWindowTitle(_translate("Train_Image", "Train_Image"))
        Train_Image.setWindowIcon(QtGui.QIcon('Icon/system_binary.ico'))
        self.label.setText(_translate("Train_Image", "     Press Train_Image"))
        self.pushButton.setText(_translate("Train_Image", "Train_Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Train_Image = QtWidgets.QDialog()
    ui = Ui_Train_Image()
    ui.setupUi(Train_Image)
    Train_Image.show()
    sys.exit(app.exec_())
