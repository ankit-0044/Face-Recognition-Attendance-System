from PyQt5 import QtCore, QtGui, QtWidgets
import yagmail

#from Project.Design.FRAS import MainWindow

class Ui_Mailwindow(object):
    def setupUi(self, Mailwindow):
        Mailwindow.setObjectName("Mailwindow")
        Mailwindow.resize(600, 397)
        self.widget = QtWidgets.QWidget(Mailwindow)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 601, 401))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:1, stop:0 rgba(131, 106, 255, 255), stop:1 rgba(255, 160, 228, 255));}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(230, 10, 161, 51))
        self.label.setStyleSheet("font: 26pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 150, 341, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(221, 153, 255);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);\n"
"    font: 12pt \"Times New Roman\";\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(87, 255, 235)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(130, 115, 271, 31))
        self.label_2.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 230, 341, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(221, 153, 255);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);\n"
"    font: 12pt \"Times New Roman\";\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(87, 255, 235)\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(130, 190, 331, 41))
        self.label_3.setStyleSheet("font: 15pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget,clicked = lambda:self.browse())
        self.pushButton.setGeometry(QtCore.QRect(480, 230, 101, 31))
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
        self.label_4.setGeometry(QtCore.QRect(255, 60, 51, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Icon/Mail.ico"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget,clicked = lambda: self.send_mail())
        self.pushButton_2.setGeometry(QtCore.QRect(230, 300, 141, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 165, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(113, 231, 255, 255), stop:1 rgba(67, 255, 183, 255));\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Mailwindow)
        QtCore.QMetaObject.connectSlotsByName(Mailwindow)

    def retranslateUi(self, Mailwindow):
        _translate = QtCore.QCoreApplication.translate
        Mailwindow.setWindowTitle(_translate("Mailwindow", "Mail"))
        Mailwindow.setWindowIcon(QtGui.QIcon("Icon/Mail.ico"))
        self.label.setText(_translate("Mailwindow", "MAIL"))
        self.label_2.setText(_translate("Mailwindow", "Receiver\'s Email.."))
        self.label_3.setText(_translate("Mailwindow", "Select Attendence File.."))
        self.pushButton.setToolTip(_translate("Mailwindow", "<html><head/><body><p>Select Your File</p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Mailwindow", "Browse"))
        self.pushButton_2.setText(_translate("Mailwindow", "SEND"))

    def browse(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName ()
        self.lineEdit_2.setText(fileName[0])
    
    def send_mail(self):
        receiver = self.lineEdit.text()  # receiver email address

        a = "Attendence" # Tittle
        loc = self.lineEdit_2.text() # Attachment Location
        body = []
        body.append(a)
        body.append(loc)

        # mail information
        Sender = 'ENTERYOUREMAIL@GMAIL.COM' 
        passwd = 'Password'
        yag = yagmail.SMTP(user=Sender,password=passwd)

        # sent the mail
        yag.send(
            to = receiver,
            subject = "Report",  # email subject
            contents  = body,  # email body
            )
        print("\n*******SENT SUCCESSFULL*******")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mailwindow = QtWidgets.QDialog()
    ui = Ui_Mailwindow()
    ui.setupUi(Mailwindow)
    Mailwindow.show()
    sys.exit(app.exec_())
