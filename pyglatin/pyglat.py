# -*- coding: utf-8 -*-

import sys
import random
from PySide import QtGui
from ui_pyglatin import Ui_pyglatin

class PyGlatinForm(Ui_pyglatin):        # наследование класса   

    def setupUi(self, pyglatin):
        super(PyGlatinForm, self).setupUi(pyglatin)
        self.pushButton.clicked.connect(self.push)

    def push(self):
        text1 = self.textEdit.toPlainText()
        word_split = text1.split()
        for i in word_split:
            pyg = random.choice ('абвгдеёжзийклмнопрстуфчцчшщцэюя')
            first = i[:1]
            new_word = i[1:]
            k = new_word + first + pyg
            self.textEdit_2.insertPlainText(k+' ')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    ui = PyGlatinForm()
    ui.setupUi(Form)
    Form.show()
    app.exec_()
    sys.exit()
