import sys

from PySide2 import QtWidgets

from mainwindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()
    app.exec_()
