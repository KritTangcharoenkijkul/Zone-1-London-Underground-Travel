import sys
import time

from astar_nextstation import *

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class StartPage(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.init_start_page()

    def init_start_page(self):
        loader = QUiLoader()
        form = loader.load("UIDesign/start_page.ui")
        self.setCentralWidget(form)
        self.setMinimumSize(1680, 900)

        self.start_button = form.findChild(QPushButton, "startBt")
        self.start_button.clicked.connect(self.changePage)

        self.hour_one_input = form.findChild(QLineEdit, "hrOne")
        self.hour_two_input = form.findChild(QLineEdit, "hrTwo")
        self.min_one_input = form.findChild(QLineEdit, "minOne")
        self.min_two_input = form.findChild(QLineEdit, "minTwo")

        self.hour_one_input.textChanged.connect(self.numberValidHour1)
        self.hour_two_input.textChanged.connect(self.numberValidHour2)
        self.min_one_input.textChanged.connect(self.numberValidMin1)
        self.min_two_input.textChanged.connect(self.numberValidMin2)
        self.updateGUI()
        self.show_hours()

        # attribute
        self.time = []


    def show_hours(self):
        #self.sender().objectName()
        hour1 = self.hour_one_input.text()
        hour2 = self.hour_two_input.text()
        min1 = self.min_one_input.text()
        min2 = self.min_two_input.text()

        print(hour1+hour2+":"+min1+min2)


    def changePage(self):
        if (self.page_time[0] == self.hour_one_input.text() and
                    self.page_time[1] == self.hour_two_input.text() and
                    self.page_time[2] == self.min_one_input.text() and
                    self.page_time[3] == self.min_two_input.text()):
            self.parent.time = "null"

        else:
            day = time.strftime("%a")
            hour = self.hour_one_input.text() + self.hour_two_input.text()
            mins = self.min_one_input.text() + self.min_two_input.text()
            self.parent.time = [day, hour, mins]
        self.parent.changePage(1)

    def numberValidMin2(self, e):
        if e.isdigit():
            if len(e) > 1:
                e = e[1]
            self.sender().setText(e)
        else:
            self.sender().setText("")
        if len(e) == 0:
            self.sender().setText("0")
            
    def numberValidMin1(self, e):
        if e.isdigit():
            if len(e) > 1:
                e = e[1]
            if int(e) > 5:
                e = '5'
            self.sender().setText(e)
        else:
            self.sender().setText("")
        if len(e) == 0:
            self.sender().setText("0")
            
    def numberValidHour2(self, e):
        if e.isdigit():
            h1 = self.hour_one_input.text()
            if len(e) > 1:
                e = e[1]
            if int(h1) == 0:
                if int(e) < 6 or int(e) > 9:
                    e = '6'
            if int(h1) == 2:
                if int(e) > 3:
                    e = '0'
                    self.hour_one_input.setText('0')
            self.sender().setText(e)
        else:
            self.sender().setText("")
        if len(e) == 0:
            self.sender().setText("0")

    def numberValidHour1(self, e):
        if e.isdigit():
            h2 = self.hour_two_input.text()
            if len(e) > 1:
                e = e[1]
            if int(e) > 2:
                e = '0'
            if e == '0':
                if int(h2) < 6 or int(h2) > 9:
                    self.hour_two_input.setText('0')
            elif e == '2':
                if int(h2) < 0 or int(h2) > 3:
                    self.hour_two_input.setText('0')
            self.sender().setText(e)
        else:
            self.sender().setText("")
        if len(e) == 0:
            self.sender().setText("0")

    def updateGUI(self):

        # update time
        day = time.strftime("%a")
        h, m = time.strftime("%H:%M").split(':')

        self.page_time = [h[0], h[1], m[0], m[1]]
        self.hour_one_input.setText(self.page_time[0])
        self.hour_two_input.setText(self.page_time[1])

        self.min_one_input.setText(self.page_time[2])
        self.min_two_input.setText(self.page_time[3])




def main():
    app = QApplication(sys.argv)

    w = StartPage()
    w.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())

