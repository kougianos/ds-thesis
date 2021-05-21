from PyQt5 import QtWidgets, QtGui
import sys
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Hello World")
        l = QtWidgets.QLabel("My simple app.")
        l.setMargin(10)
        self.setCentralWidget(l)

        self.setWindowIcon(QtGui.QIcon('neural.png'))
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('neural.png'))
    w = MainWindow()
    trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("neural.png"), app)
    trayIcon.show()
    app.exec()
