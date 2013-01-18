# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keydialog.ui'
#
# Created: Fri Jan 18 12:46:40 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_KeyDialog(object):
    def setupUi(self, KeyDialog):
        KeyDialog.setObjectName("KeyDialog")
        KeyDialog.resize(219, 40)
        KeyDialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        KeyDialog.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralWidget = QtGui.QWidget(KeyDialog)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 10, 51, 24))
        self.pushButton.setObjectName("pushButton")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 61, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 81, 23))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit.setObjectName("lineEdit")
        KeyDialog.setCentralWidget(self.centralWidget)

        self.retranslateUi(KeyDialog)
        QtCore.QMetaObject.connectSlotsByName(KeyDialog)

    def retranslateUi(self, KeyDialog):
        KeyDialog.setWindowTitle(QtGui.QApplication.translate("KeyDialog", "Enter Your Key", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("KeyDialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("KeyDialog", "Enter key", None, QtGui.QApplication.UnicodeUTF8))

