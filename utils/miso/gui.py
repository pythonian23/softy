from PyQt5 import QtWidgets, uic


class Miso(QtWidgets.QMainWindow):
    def __init__(self):
        super(Miso, self).__init__()
        uic.loadUi("main.ui", self)
        self.show()
