from PySide import QtGui
from form_caesar import Ui_MainWindow
from keydialog import Ui_KeyDialog
import sys

class DialogForm(Ui_KeyDialog):

    def setupUi(self,KeyDialog):
        super().setupUi(KeyDialog)
        self.pushButton.clicked.connect(self.set_key)
        self.window = KeyDialog

    def set_key(self):
        self.key = self.lineEdit.text()
        if self.key.isdigit():
        #print ('hui')
            self.window.close()
            return int(self.key)
        else:
            msg = QtGui.QMessageBox()
            msg.setText('fuck')
            msg.setWindowTitle('FUCK')
            msg.exec_()


class CaesarForm(Ui_MainWindow):

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.crypt.clicked.connect(self.crypt_push)
        self.decrypt.clicked.connect(self.decrypt_push)
        self.keybutton.clicked.connect(self.key_enter)
        self.dia = QtGui.QMainWindow()
        self.ui1 = DialogForm()
        self.ui1.setupUi(self.dia)

    def __init__(self):

        global alphabet

        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', \
                         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


    def key_enter(self):

        self.dia.show()

    def crypt_push(self):

        if not hasattr(self, "ui1"):
            self.safety_key=0
        else:
            self.safety_key = self.ui1.set_key()
        print (self.safety_key)

        trans = ''
        text = self.get_message()
        print (text)

        for symbol in text:
            if symbol in self.alphabet:
                num = (self.alphabet.index(symbol)+self.safety_key)%52
                trans += self.alphabet[num]
            else:
                trans += symbol

        self.NextText.insertPlainText(trans)
        print (trans)

    def decrypt_push(self):

        try:
            self.safety_key = self.ui1.set_key()
        except:
            self.safety_key = 0
        print (self.safety_key)

        trans = ''
        text = self.get_message()

        for symbol in text:
            if symbol in self.alphabet:
                num = (self.alphabet.index(symbol)-self.safety_key)%52
                trans += self.alphabet[num]
            else:
                trans += symbol

        self.NextText.insertPlainText(trans)

    def get_message(self):
        get_text = self.MainText.toPlainText()
        return get_text


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    ui = CaesarForm()
    ui.setupUi(Form)
    Form.show()
    app.exec_()
    sys.exit()
