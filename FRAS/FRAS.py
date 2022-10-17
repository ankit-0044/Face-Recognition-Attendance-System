from PyQt5 import QtCore, QtGui, QtWidgets
import check_camera 
from Stu_Dtl import Ui_Dialog
from Mail import Ui_Mailwindow
from Train_Image_ui import Ui_Train_Image
from time import sleep
import Recognize

class Ui_MainWindow(object):
    
    # Checking camera function....   
    def checkCamera(self):
            check_camera.camer()
            sleep(0.0009)
            return 0

    # Register Student Detail window
    def StudentDetail(self):
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog ()
            self.ui.setupUi(self.window)
            self.window.show()

    # Train image function        
    def train_image(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Train_Image ()
        self.ui.setupUi(self.window)
        self.window.show()

    # Mark Attendence Fuction
    def attend(self):
        Recognize.recognize_attendence()

    def Mail(self):
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Mailwindow ()
            self.ui.setupUi(self.window)
            self.window.show()
    
    # Exit 
    def exit_window(self):
        exit()    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 625)
        MainWindow.setMaximumSize(QtCore.QSize(800, 625))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 625))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 625))
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(800, 625))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0.167464 rgba(114, 56, 255, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.widget.setObjectName("widget")

        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 70, 801, 20))
        self.line.setMaximumSize(QtCore.QSize(820, 100))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 0, 661, 81))
        self.label.setStyleSheet("font: 18pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.verticalWidget = QtWidgets.QWidget(self.widget)
        self.verticalWidget.setGeometry(QtCore.QRect(290, 90, 211, 501))
        self.verticalWidget.setObjectName("verticalWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.check_camera = QtWidgets.QPushButton(self.verticalWidget, clicked = lambda :self.checkCamera())
        self.check_camera.setMaximumSize(QtCore.QSize(200, 40))
        self.check_camera.setToolTipDuration(1)
        self.check_camera.setAutoFillBackground(False)
        self.check_camera.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.check_camera.setObjectName("check_camera")
        self.verticalLayout.addWidget(self.check_camera)

        self.register_2 = QtWidgets.QPushButton(self.verticalWidget, clicked = lambda : self.StudentDetail())
        self.register_2.setMaximumSize(QtCore.QSize(200, 40))
        self.register_2.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.register_2.setObjectName("register_2")
        self.verticalLayout.addWidget(self.register_2)

        self.train = QtWidgets.QPushButton(self.verticalWidget,clicked = lambda :self.train_image())
        self.train.setMaximumSize(QtCore.QSize(200, 40))
        self.train.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.train.setObjectName("train")
        self.verticalLayout.addWidget(self.train)

        self.attendance = QtWidgets.QPushButton(self.verticalWidget, clicked =lambda:self.attend())
        self.attendance.setMaximumSize(QtCore.QSize(200, 40))
        self.attendance.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.attendance.setObjectName("attendance")
        self.verticalLayout.addWidget(self.attendance)

        self.mail = QtWidgets.QPushButton(self.verticalWidget, clicked = lambda: self.Mail())
        self.mail.setMaximumSize(QtCore.QSize(200, 40))
        self.mail.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.mail.setObjectName("mail")
        self.verticalLayout.addWidget(self.mail)

        self.exit_button = QtWidgets.QPushButton(self.verticalWidget, clicked = lambda :self.exit_window())
        self.exit_button.setMaximumSize(QtCore.QSize(200, 40))
        self.exit_button.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(720, 10, 61, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Icon/facial-recognition.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(240, 130, 40, 40))
        self.label_5.setMinimumSize(QtCore.QSize(40, 40))
        self.label_5.setMaximumSize(QtCore.QSize(40, 40))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Icon/webcam.ico"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(240, 200, 40, 40))
        self.label_6.setMinimumSize(QtCore.QSize(40, 40))
        self.label_6.setMaximumSize(QtCore.QSize(40, 40))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Icon/id.ico"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(240, 280, 40, 40))
        self.label_7.setMinimumSize(QtCore.QSize(40, 40))
        self.label_7.setMaximumSize(QtCore.QSize(40, 40))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Icon/system_binary.ico"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(240, 360, 40, 40))
        self.label_8.setMinimumSize(QtCore.QSize(40, 40))
        self.label_8.setMaximumSize(QtCore.QSize(40, 40))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Icon/Inipagi-Business-Economic-Checklist.ico"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(240, 440, 40, 40))
        self.label_9.setMinimumSize(QtCore.QSize(40, 40))
        self.label_9.setMaximumSize(QtCore.QSize(40, 40))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Icon/mail.ico"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(240, 510, 40, 40))
        self.label_10.setMinimumSize(QtCore.QSize(40, 40))
        self.label_10.setMaximumSize(QtCore.QSize(40, 40))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Icon/gnome_panel_force_quit.ico"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(8, 20, 51, 41))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Icon/ptu_logo.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FRAS"))
        MainWindow.setWindowIcon(QtGui.QIcon("Icon/facial-recognition.png"))
        self.label.setText(_translate("MainWindow", "FACE RECOGNITION ATTENDANCE SYSTEM"))
        self.check_camera.setToolTip(_translate("MainWindow", "<html><head/><body><p>On Camera</p></body></html>"))
        self.check_camera.setStatusTip(_translate("MainWindow", "This is status tip"))
        self.check_camera.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Check Your Camera Connect !</p></body></html>"))
        self.check_camera.setText(_translate("MainWindow", "Check Camera"))
        self.register_2.setText(_translate("MainWindow", "Register Student"))
        self.train.setText(_translate("MainWindow", "Train Images"))
        self.attendance.setText(_translate("MainWindow", "Attendance"))
        self.mail.setText(_translate("MainWindow", "Mail"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
