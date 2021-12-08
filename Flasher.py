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

        self.pushButton.pressed.connect(lambda: GPIO.output(40,1))

        self.pushButton.released.connect(lambda: GPIO.output(40,0))


        GPIO.add_event_detect(17, GPIO.BOTH)

    # def on(self):
    #     self.checkBox.setChecked(1)

    # def off(self):
    #     self.checkBox.setChecked(0)

        try:
            while True:
                if GPIO.event_detected(17):
                    
                    if self.checkBox.checkState() == 1:
                        self.checkBox.setChecked(0)

                    else:
                        self.checkBox.setChecked(1)

                    
        except KeyboardInterrupt:
            pass

        
if __name__ == '__main__':

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.OUT)
    GPIO.setup(17,GPIO.IN)

    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())