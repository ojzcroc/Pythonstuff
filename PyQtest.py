#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows a tooltip on 
a window and a button

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtCore 
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

exitYesNo = "No"

class Window(QtGui.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

        
    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        btn = QtGui.QPushButton('Start', self)
        btn.setToolTip('Press to start')
        btn.resize(btn.sizeHint())
        btn.move(95,65)

        btn2 = QtGui.QPushButton('Autoexit?', self)
        btn2.setToolTip('Do you want to exit Timed Tables automatically when done?')
        btn2.resize(btn.sizeHint())
        btn2.setCheckable(True)
        btn2.move(95,105)

        btn2.clicked[bool].connect(self.buttonClicked2)

        self.le = QtGui.QLineEdit(self)
        self.le.move(15, 22)
        self.le.setToolTip('How many times do you want the program to repeat?')

        self.le2 = QtGui.QLineEdit(self)
        self.le2.move(145, 22)
        self.le2.setToolTip('What name do you want on the leaderboard?')

        self.resize(250, 150)
        self.center()

        btn.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked2)

        self.setWindowTitle('TimedTablesCheat')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.setGeometry(300, 300, 290, 150)

        self.show()

    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttonClicked(self):
        print self.le.text()
        print self.le2.text()
        global exitYesNo
        print exitYesNo
        
    def buttonClicked2(self,pressed):
        global exitYesNo
        if pressed:
            exitYesNo = "Yes"
        else:
            exitYesNo = "No"
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

