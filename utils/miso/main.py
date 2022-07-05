import sys
from PyQt5 import QtWidgets
import gui

app = QtWidgets.QApplication(sys.argv)
window = gui.Miso()
app.exec_()
