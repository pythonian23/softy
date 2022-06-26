import sys

from PyQt5 import QtCore, QtGui, QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    widget.setWindowTitle("MISO: Make Interesting Softy Objects")
    label = QtWidgets.QLabel(widget)
    label.setText("MISO: Make Interesting Softy Objects")
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
