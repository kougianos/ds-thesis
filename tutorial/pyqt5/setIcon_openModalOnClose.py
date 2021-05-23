import ctypes
import sys

from PyQt5 import QtWidgets, QtGui

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Hello World")
        label = QtWidgets.QLabel("My simple app.")
        label.setMargin(10)
        self.setCentralWidget(label)
        self.setWindowIcon(QtGui.QIcon('neural.png'))

        self.show()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            'Message', "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    app.exec()
