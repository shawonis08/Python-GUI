import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets

qtCreatorFile = "panel.ui"  # Enter file here.
loginFile = "login.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType( qtCreatorFile )

LoginWindowUI, LoginWindow = uic.loadUiType( loginFile )


class MyApp( QtWidgets.QMainWindow, Ui_MainWindow ):
    def __init__(self):
        QtWidgets.QMainWindow.__init__( self )
        Ui_MainWindow.__init__( self )
        self.setupUi( self )
        self.LoginButton.clicked.connect( self.loginWindow )

    def loginWindow(self):
        self.hide()
        self.child_win = Login(self)
        self.child_win.show()


class Login( LoginWindow, LoginWindowUI ):
    def __init__(self, parent=None):
        LoginWindow.__init__(self, parent)
        self.setupUi(self)
        self.cancelButton.clicked.connect(self.cancelWindow)

    def cancelWindow(self):
        self.terminate()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv )
    window = MyApp()
    window.show()
sys.exit( app.exec_() )