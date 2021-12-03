import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtWidgets
from Flash import Ui_MainWindow


import RPi.GPIO as GPIO  # import GPIO

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.pressed.connect(lambda: self.on())

        self.pushButton.released.connect(lambda: self.off())

    def on(self):
        self.checkBox.setChecked(1)
        GPIO.output(40,1)

    def off(self):
        self.checkBox.setChecked(0)
        GPIO.output(40,0)


if __name__ == '__main__':

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(40, GPIO.OUT)

    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
