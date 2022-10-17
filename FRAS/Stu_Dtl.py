import csv
import cv2
import os

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def Capture_Face(self):
        name = self.lineEdit.text()
        Id = self.lineEdit_2.text()

        if(self.is_number(Id) and name.isalpha()):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0

            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
                for(x,y,w,h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                    #incrementing sample number
                    sampleNum = sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage" + os.sep +name + "."+Id + '.' +
                                str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                    #display the frame
                    cv2.imshow('frame', img)
                #wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is more than 100
                elif sampleNum > 100:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Saved for ID : " + Id + " Name : " + name
            row = [Id, name]
            with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
        else:
            if(self.is_number(Id)):
                print("Enter Alphabetical Name")
            if(name.isalpha()):
                print("Enter Numeric ID")


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 500)
        Dialog.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 601, 501))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:1, stop:0 rgba(131, 106, 255, 255), stop:1 rgba(255, 160, 228, 255));}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(140, 30, 351, 61))
        self.label.setStyleSheet("font: 24pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(170, 150, 131, 31))
        self.label_2.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(170, 250, 150, 31))
        self.label_3.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 180, 261, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(221, 153, 255);\n"
"border-radius: 15px;\n"
"color: rgb(0,0,0);\n"
"    font: 12pt \"Times New Roman\";\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(87, 255, 235)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 280, 261, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(221, 153, 255);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0,0);\n"
"    font: 12pt \"Times New Roman\";\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(87, 255, 235)\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.Capture_Face())
        self.pushButton.setGeometry(QtCore.QRect(270, 370, 151, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(180, 370, 61, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Icon\\facial-recognition.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Student Details"))
        Dialog.setWindowIcon(QtGui.QIcon("Icon\id.ico"))
        self.label.setText(_translate("Dialog", "STUDENT DETAILS"))
        self.label_2.setText(_translate("Dialog", "Student Name"))
        self.label_3.setText(_translate("Dialog", "Student Roll No"))
        self.pushButton.setText(_translate("Dialog", "Capture Face"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
