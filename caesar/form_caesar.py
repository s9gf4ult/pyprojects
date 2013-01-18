# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jan 18 09:34:36 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 290)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.MainText = QtGui.QPlainTextEdit(self.centralWidget)
        self.MainText.setGeometry(QtCore.QRect(10, 10, 391, 111))
        self.MainText.setObjectName("MainText")
        self.NextText = QtGui.QPlainTextEdit(self.centralWidget)
        self.NextText.setGeometry(QtCore.QRect(10, 130, 391, 121))
        self.NextText.setReadOnly(True)
        self.NextText.setObjectName("NextText")
        self.crypt = QtGui.QPushButton(self.centralWidget)
        self.crypt.setGeometry(QtCore.QRect(320, 260, 80, 24))
        self.crypt.setObjectName("crypt")
        self.decrypt = QtGui.QPushButton(self.centralWidget)
        self.decrypt.setGeometry(QtCore.QRect(220, 260, 80, 24))
        self.decrypt.setObjectName("decrypt")
        self.keybutton = QtGui.QPushButton(self.centralWidget)
        self.keybutton.setGeometry(QtCore.QRect(10, 260, 80, 24))
        self.keybutton.setObjectName("keybutton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Caesar Cipher", None, QtGui.QApplication.UnicodeUTF8))
        self.crypt.setText(QtGui.QApplication.translate("MainWindow", "Crypt", None, QtGui.QApplication.UnicodeUTF8))
        self.decrypt.setText(QtGui.QApplication.translate("MainWindow", "DeCrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.keybutton.setText(QtGui.QApplication.translate("MainWindow", "Key", None, QtGui.QApplication.UnicodeUTF8))

