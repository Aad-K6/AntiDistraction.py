from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox,QLineEdit
from TabMainPages import Ui_MainWindow
from WebBlock import Ui_MainWindow1
from ReminderCustom import Ui_MainWindow2
from todolist import Ui_MainWindow3
from Testing import Ui_MainWindow4
from plyer import notification
import time
import threading
import sys


class TabWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent = TabWindow


        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 932, 765))  #set the dimentions of tab widget
        self.tabWidget.setStyleSheet("background-image: url(:/img/sunset.png);") #adding stylesheet to tab widget

        self.tabWidget.setObjectName("tab")
        self.starting = QtWidgets.QWidget()
        self.starting.setObjectName("starting")
        self.tabWidget.addTab(starting(), "Starting") # change tab name

        self.webblockerpage= QtWidgets.QWidget()
        self.webblockerpage.setObjectName("webblockerpage")
        self.tabWidget.addTab(webblockerpage(), " WebBlocker ")  # tab button added for website blocker

        self.reminderpage = QtWidgets.QWidget()
        self.reminderpage.setObjectName("reminderpage")
        self.tabWidget.addTab(reminderpage(), "Reminder") #Reminder tab button

        self.todolistpage = QtWidgets.QWidget()
        self.todolistpage.setObjectName("todolistpage")
        self.tabWidget.addTab(todolistpage(), "To do list") #to do list tab button


class webblockerpage(QtWidgets.QMainWindow):  #calling Web block page into tab 2 ,
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(90, 290, 721, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:30px;\n"
                                    "color:white;\n"
                                    "padding:9px;"
                                    "background-image: url(:/img/sunset.png);")

        self.ui.blockButton.clicked.connect(self.blockWeb)
        self.ui.unblockButton.clicked.connect(self.unblockWeb)

    def blockWeb(self):
        hosts_path = "C:\Windows\System32\drivers\etc\hosts"
        redirect = "127.0.0.1"
        website_list =[self.lineEdit.text()]
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect + " " + website)

    def unblockWeb(self):
        hosts_path = "C:\Windows\System32\drivers\etc\hosts"
        redirect = "127.0.0.1"
        website_list = [self.lineEdit.text()]
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()



class reminderpage(QtWidgets.QMainWindow):  #calling reminder page into tab 3 ,
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

#for custom reminder time interval
        self.customTimeLine = QtWidgets.QLineEdit(self)
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
                                          "padding:9px;"
                                          "background-image: url(:/img/sunset.png);")
        self.customTimeLine.setPlaceholderText("Enter time interval in minutes")

        #for text message to be displayed
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
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
                                      "padding:9px;"
                                      "background-image: url(:/img/sunset.png);")
        self.lineEdit_3.setPlaceholderText("Enter message to be displayed")

        #event calling buttons
        self.ui.CustomTimeBut.clicked.connect(self.CustomReminder)


    def CustomReminder(self):
        interval = float(self.customTimeLine.text())*60
        mess = self.lineEdit_3.text()
        breakcount = 0
        finalcount = 3
        while (breakcount < finalcount):
            notification.notify(title=' ', message=f'{mess}', timeout=3)
            time.sleep(interval)
            breakcount += 1


class todolistpage(QtWidgets.QMainWindow):  #calling to do list page into tab 4 ,
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)

        self.loadTasks()
        self.ui.AddToList.clicked.connect(self.AddTask)
        self.ui.DelFromList.clicked.connect(self.DeleteTask)
        self.ui.EditButton.clicked.connect(self.EditTask)
        self.ui.SortButton.clicked.connect(self.SortTask)


    def loadTasks(self):
        self.ui.listWidget.addItems([' '])
        self.ui.listWidget.setCurrentRow(0)


    def AddTask(self):
        currentIndex = self.ui.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, "New Tasks", "TASK NAME: ")
        if ok and text is not None:
            self.ui.listWidget.insertItem(currentIndex, text)


    def DeleteTask(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)
        if item is None:
            return
        question = QMessageBox.question(self, "Delete Task", "\nTASK COMPLETED?\n" + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.ui.listWidget.takeItem(currentIndex)
            del item


    def EditTask(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)
        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Task", "TASK NAME: ", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)


    def SortTask(self):
        self.ui.listWidget.sortItems()


class starting(QtWidgets.QMainWindow):  #calling intro page into tab 1.
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 130, 480, 105))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(39)
        self.label.setFont(font)

        self.label.setStyleSheet("\n"
                                 "QLabel {\n"
                                 "    color: white;\n"
                                 "    border-style: inset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 30px;\n"
                                 "    border-color: beige;\n"
                                 "    padding: 9px;\n"
                                 "    \n"
                                 "}")

        self.label.setText(QtCore.QDate.currentDate().toString())

        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 245, 480, 65))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(30)
        self.label_2.setFont(font)

        self.label_2.setStyleSheet("\n"
                                   "QLabel {\n"
                                   "    color: white;\n"
                                   "    border-style: inset;\n"
                                   "    border-width: 2px;\n"
                                   "    border-radius: 30px;\n"
                                   "    border-color: beige;\n"
                                   "    padding: 9px;\n"
                                   "    \n"
                                   "}")

        self.label_2.setText(QtCore.QTime.currentTime().toString())

        self.label_2.setObjectName("label_2")

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = TabWindow()
    MainWindow.show()
    app.exec_()