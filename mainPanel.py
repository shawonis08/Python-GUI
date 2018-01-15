import sys
from PyQt5 import uic,QtWidgets

# qtInputFile variable expect ui file as input
qtInputFile = "mainPanel.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType( qtInputFile )