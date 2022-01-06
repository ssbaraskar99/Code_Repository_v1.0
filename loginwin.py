from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
# creating global variable luser(loggedinuser)
# this will be passed to homepage search submission window
global loggedinuser
loggedinuser=""
import sys
#importing everything from homepagewin
from homepagewin import *
import os.path
from pathlib import Path
#imported especially for Shadow effect
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

# making connection & cursor object for login window
logincon=sqlite3.connect('coderepo.db')
logincur=logincon.cursor()

class Ui_loginwin(object):
# dologin function to do login , connected a1to loginbtn ----------------------------------------------------------------------------------------
    def dologin(self):
        print("login btn clicked !")
        try:
            if self.usernametxtbx.text()!="" and self.passwordtxtbx.text()!="":
                logincur.execute('''select * from Users where username=(?) and password=(?);''',(self.usernametxtbx.text(),self.passwordtxtbx.text()))
                logincon.commit()
                temp=logincur.fetchall()
                result=[item for t in temp for item in t]
                if len(result)!=0:
                    if result[0]==self.usernametxtbx.text() and result[1]==self.passwordtxtbx.text():
                        loggedinuser=self.usernametxtbx.text()
                        print("Login Success")
                        # calling setupui function from homepage file
                        self.window=QtWidgets.QMainWindow()
                        # now passing username to the init function
                        #in homepagewin which will set luser
                        self.hpg=Ui_homepagewin(self.usernametxtbx.text())
                        self.hpg.setupUi(self.window)
                        self.window.show()
                        loginwin.close()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setWindowIcon(QtGui.QIcon('icon.png'))
                        msg.setText("No User Exits")
                        font = QtGui.QFont()
                        font.setFamily("Poppins")
                        font.setPointSize(11)
                        font.setWeight(57)
                        msg.setFont(font)
                        msg.setInformativeText('You Need to create a Account\n Using Register Button, then try to Login !')
                        msg.setWindowTitle("ERROR")
                        msg.exec_()
                else:
                    self.usernametxtbx.setText("")
                    self.passwordtxtbx.setText("")
                    msg = QMessageBox()
                    font = QtGui.QFont()
                    font.setFamily("Poppins")
                    font.setPointSize(11)
                    font.setWeight(57)
                    msg.setFont(font)
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(QtGui.QIcon('icon.png'))
                    msg.setText("No User Exits")
                    msg.setInformativeText('You Need to create a Account\n Using Register Button, then try to Login !')
                    msg.setWindowTitle("ERROR")
                    msg.exec_()
            else:
                self.usernametxtbx.setText("")
                self.passwordtxtbx.setText("")
                msg = QMessageBox()
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(11)
                font.setWeight(57)
                msg.setFont(font)
                msg.setWindowIcon(QtGui.QIcon('icon.png'))
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Field Empty")
                msg.setInformativeText('You have missed filling credentials ! \nPlease Enter Login Credentials')
                msg.setWindowTitle("ERROR")
                msg.exec_()
        except Exception as e:
            print(e)
# do regsiter function , connected to registerbtn
    def doregister(self):
        try:
            print("registr func called !")
            if self.usernametxtbx.text()!="" and self.passwordtxtbx.text()!="":
                print(self.usernametxtbx.text())
                print(self.passwordtxtbx.text())
                logincur.execute('''insert into users values (?,?)''',[self.usernametxtbx.text(),self.passwordtxtbx.text()])
                logincon.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(11)
                font.setWeight(57)
                msg.setFont(font)
                msg.setWindowIcon(QtGui.QIcon('icon.png'))
                msg.setText("Successfully Registered !")
                msg.setInformativeText('You Have Been Registered ! \nPlease Login through your Credentials')
                msg.setWindowTitle("Registration Complete")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(11)
                font.setWeight(57)
                msg.setFont(font)
                msg.setWindowIcon(QtGui.QIcon('icon.png'))
                msg.setText("Field Empty")
                msg.setInformativeText('You have missed filling credentials ! \nPlease Enter Login Credentials')
                msg.setWindowTitle("ERROR")
                msg.exec_()
        except Exception as e:
            print(e)
            # e = "UNIQUE constraint failed: Users.username" when username is present in db
            if str(e)=="UNIQUE constraint failed: Users.username":
                self.usernametxtbx.setText("")
                self.passwordtxtbx.setText("")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(11)
                font.setWeight(57)
                msg.setFont(font)
                msg.setWindowIcon(QtGui.QIcon('icon.png'))
                msg.setText("User Already Exits !")
                msg.setInformativeText('You Have Not Been Registered ! \nPlease use different Username')
                msg.setWindowTitle("ERROR")
                msg.exec_()

#   this function is called to load ui
# generated by converting ui file
    def setupUi(self, loginwin):

        # here im setting font file location
        # so that enduser needs not to install font
        QtGui.QFontDatabase.addApplicationFont("Poppins-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont("Poppins-Regular.ttf")
        loginwin.setObjectName("loginwin")
        loginwin.setWindowModality(QtCore.Qt.ApplicationModal)
        loginwin.resize(1280, 720)
        loginwin.setMinimumSize(QtCore.QSize(1280, 720))
        loginwin.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        #this is app icon file
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginwin.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        loginwin.setFont(font)
        loginwin.setStyleSheet("background-color:#2e2e2e;")
        self.centralwidget = QtWidgets.QWidget(loginwin)
        self.centralwidget.setObjectName("centralwidget")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 751, 721))
        self.frame1.setToolTipDuration(-1)
        self.frame1.setStyleSheet("background-color: rgb(108, 99, 255);\n"
"border-radius: 0px  20px 20px 0px;")
        self.frame1.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setObjectName("frame1")
        self.usernametxtbx = QtWidgets.QLineEdit(self.frame1)
        self.usernametxtbx.setGeometry(QtCore.QRect(70, 250, 391, 41))
        self.usernametxtbx.setStyleSheet("background-color:#2e2e2e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font-size:14px;\n"
"font-family:Poppins;\n"
"font-weight:light;\n"
"padding:4px;\n"
"padding-left:12px;\n"
"")
        self.usernametxtbx.setClearButtonEnabled(True)
        self.usernametxtbx.setObjectName("usernametxtbx")

        shadow = QGraphicsDropShadowEffect(blurRadius=4, xOffset=2, yOffset=2)
        shadow.setColor(Qt.black)
        self.usernametxtbx.setGraphicsEffect(shadow)

        self.passwordtxtbx = QtWidgets.QLineEdit(self.frame1)
        self.passwordtxtbx.setGeometry(QtCore.QRect(70, 330, 391, 41))
        self.passwordtxtbx.setStyleSheet("background-color:#2e2e2e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font-size:14px;\n"
"font-family:Poppins;\n"
"font-weight:light;\n"
"padding:4px;\n"
"padding-left:12px;")
        self.passwordtxtbx.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordtxtbx.setClearButtonEnabled(False)
        self.passwordtxtbx.setObjectName("passwordtxtbx")

        shadow = QGraphicsDropShadowEffect(blurRadius=4, xOffset=2, yOffset=2)
        shadow.setColor(Qt.black)
        self.passwordtxtbx.setGraphicsEffect(shadow)

        self.coderepolbl = QtWidgets.QLabel(self.frame1)
        self.coderepolbl.setGeometry(QtCore.QRect(70, 160, 301, 51))
        self.coderepolbl.setStyleSheet("color:#2e2e2e;\n"
"border-radius:10px;\n"
"font-size:35px;\n"
"font-family:Poppins;\n"
"font-weight:bold;\n"
"")
        self.coderepolbl.setObjectName("coderepolbl")
        self.loginbtn = QtWidgets.QPushButton(self.frame1)
        self.loginbtn.setGeometry(QtCore.QRect(350, 410, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginbtn.sizePolicy().hasHeightForWidth())
        self.loginbtn.setSizePolicy(sizePolicy)
        self.loginbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginbtn.setStyleSheet("background-color:#2e2e2e;\n"
"border-radius:10px;\n"
"color:rgb(108, 99, 255);\n"
"font-size:20px;\n"
"font-family:Poppins;\n"
"font-weight:bold;\n"
"\n"
"")
        self.loginbtn.setObjectName("loginbtn")
        #loginbtn click event
        self.loginbtn.clicked.connect(self.dologin)

        shadow = QGraphicsDropShadowEffect(blurRadius=6, xOffset=4, yOffset=4)
        shadow.setColor(Qt.black)
        self.loginbtn.setGraphicsEffect(shadow)

        self.registerbtn = QtWidgets.QPushButton(self.frame1)
        self.registerbtn.setGeometry(QtCore.QRect(180, 410, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerbtn.sizePolicy().hasHeightForWidth())
        self.registerbtn.setSizePolicy(sizePolicy)
        self.registerbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerbtn.clicked.connect(self.doregister)
        self.registerbtn.setToolTipDuration(-1)
        self.registerbtn.setStyleSheet("background-color:#bfbfbf;\n"
"border-radius:10px;\n"
"color:#2e2e2e;\n"
"font-size:20px;\n"
"font-family:Poppins;\n"
"font-weight:bold;\n"
"\n"
"\n"
"")
        self.registerbtn.setObjectName("registerbtn")

        shadow = QGraphicsDropShadowEffect(blurRadius=6, xOffset=4, yOffset=4)
        shadow.setColor(Qt.black)
        self.registerbtn.setGraphicsEffect(shadow)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(790, 440, 451, 261))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("loginpageimg.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        loginwin.setCentralWidget(self.centralwidget)
        self.retranslateUi(loginwin)
        QtCore.QMetaObject.connectSlotsByName(loginwin)

    def retranslateUi(self, loginwin):
        _translate = QtCore.QCoreApplication.translate
        loginwin.setWindowTitle(_translate("loginwin", "Code repository :Login Page"))
        self.usernametxtbx.setPlaceholderText(_translate("loginwin", "Username"))
        self.passwordtxtbx.setPlaceholderText(_translate("loginwin", "Password"))
        self.coderepolbl.setText(_translate("loginwin", "Code Repository"))
        self.loginbtn.setToolTip(_translate("loginwin", "<html><head/><body style=\"font-weight:Regular;font-size:14px;\">\n"
"\n"
"<span >\n"
"<p >Enter your login credentials &amp; click Login !</p>\n"
"</span>\n"
"</body></html>"))
        self.loginbtn.setText(_translate("loginwin", "Login"))
        self.registerbtn.setToolTip(_translate("loginwin", "<html><head/><body><p><span style=\" font-size:14px;\">If you are New User without any credentials then,</span></p><p><span style=\" font-size:14px;\">To becaome a User ,</span></p><p><span style=\" font-size:14px;\">Enter a Username &amp; Password then click Register. </span></p></body></html>"))
        self.registerbtn.setText(_translate("loginwin", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginwin = QtWidgets.QMainWindow()
    ui = Ui_loginwin()
    ui.setupUi(loginwin)
    loginwin.show()
    sys.exit(app.exec_())
