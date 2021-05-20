import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, )


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setMinimumHeight(600)
        self.setMinimumWidth(600)

        widget = QLabel("Hello")
        widget.setStyleSheet("margin: auto 25px auto; "
                             "padding-bottom: 50%; "
                             "border: 2px solid red; "
                             "border-radius: 50px"
                             )
        font = widget.font()
        font.setPointSize(30)
        font.setBold(True)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
