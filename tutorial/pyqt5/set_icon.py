from PyQt5 import QtWidgets, QtGui
import sys
import ctypes

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction

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
            self.tray_icon.show()
            self.hide()
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('neural.png'))
    app.setQuitOnLastWindowClosed(False)
    w = MainWindow()

    # Adding an icon
    icon = QIcon("neural.png")

    # Adding item on the menu bar
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Creating the options
    menu = QMenu()
    option1 = QAction("My App")
    menu.addAction(option1)

    # To quit the app
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Adding options to the System Tray
    tray.setContextMenu(menu)

    app.exec()
