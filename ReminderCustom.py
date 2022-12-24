# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReminderCustom.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/img/sunset.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.backforwb = QtWidgets.QPushButton(self.centralwidget)
        self.backforwb.setGeometry(QtCore.QRect(0, 0, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.backforwb.setFont(font)
        self.backforwb.setStyleSheet("color: beige;\n"
"border-style: groove;\n"
"border-width: 1px;\n"
"border-color:beige;\n"
"")
        self.backforwb.setObjectName("backforwb")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 150, 541, 81))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"padding:1px;")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.customTimeLine = QtWidgets.QLineEdit(self.centralwidget)
        self.customTimeLine.setGeometry(QtCore.QRect(160, 260, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.customTimeLine.setFont(font)
        self.customTimeLine.setStyleSheet("border-radius:20px;\n"
"color:white;\n"
"padding:9px;")
        self.customTimeLine.setText("")
        self.customTimeLine.setObjectName("customTimeLine")
        self.CustomTimeBut = QtWidgets.QPushButton(self.centralwidget)
        self.CustomTimeBut.setGeometry(QtCore.QRect(380, 460, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CustomTimeBut.setFont(font)
        self.CustomTimeBut.setStyleSheet("border-style: outset;\n"
"border-width: 4px;\n"
"border-radius:15px;\n"
"border-color: beige;\n"
"padding: 9px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.CustomTimeBut.setObjectName("CustomTimeBut")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 330, 611, 111))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:20px;\n"
"color:white;\n"
"padding:9px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backforwb.setText(_translate("MainWindow", "back"))
        self.label_2.setText(_translate("MainWindow", "             .CUSTOM REMINDER."))
        self.CustomTimeBut.setText(_translate("MainWindow", "SET"))
import Resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
