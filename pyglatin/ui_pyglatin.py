# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Oct 17 11:56:20 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_pyglatin(object):
    def setupUi(self, pyglatin):
        pyglatin.setObjectName("pyglatin")
        pyglatin.resize(322, 256)
        self.centralWidget = QtGui.QWidget(pyglatin)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 83, 25))
        self.pushButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 100, 301, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 301, 71))
        self.textEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit.setObjectName("textEdit")
        pyglatin.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(pyglatin)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 322, 22))
        self.menuBar.setObjectName("menuBar")
        pyglatin.setMenuBar(self.menuBar)

        self.retranslateUi(pyglatin)
        QtCore.QMetaObject.connectSlotsByName(pyglatin)

    def retranslateUi(self, pyglatin):
        pyglatin.setWindowTitle(QtGui.QApplication.translate("pyglatin", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("pyglatin", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

