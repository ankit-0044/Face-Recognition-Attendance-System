import os
import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import Qt
from FRASmain import Ui_MainWindow
import check_camera
import Capture_Image
import Train_Image
import Recognize
import csv
import cv2
import os

#import main

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        loadUi('./FRAS.ui',self)
        self.check_camera.clicked.connect(self.checkCamera)
        self.register_2.clicked.connect(self.register)
        self.train.clicked.connect(self.train_image)
        self.attendance.clicked.connect(self.attend)
        self.mail.clicked.connect(self.send_mail)
        self.exit_button.clicked.connect(self.exit_window)
        #self.show()

    def checkCamera(self):
        check_camera.camer()
        #key = input("Enter any key to return main menu ")
        #sys.exit()
        widget.show()

    def register(self):
        #Capture_Image.takeImages()
        #key = input("Enter any key to return main menu ")
        def is_number(s):
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



# Take image function

        def takeImages():


            Id = input("Enter Your Id: ")
            name = input("Enter Your Name: ")

            if(is_number(Id) and name.isalpha()):
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
                if(is_number(Id)):
                    print("Enter Alphabetical Name")
                if(name.isalpha()):
                    print("Enter Numeric ID")
        takeImages()

    def train_image(self):
        Train_Image.TrainImages()
        #key = input("Enter any key to return main menu ")
        widget.show()

    def attend(self):
        Recognize.recognize_attendence()
        #key = input("Enter any key to return main menu ")
        widget.show()

    def send_mail(self):
        os.system('py automail.py')
        widget.show()

    def exit_window(self):
        exit()
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    widget = QStackedWidget()
    widget.addWidget(window)
    widget.setFixedHeight(700)
    widget.setFixedWidth(800)
    widget.show()

    app.exec()
