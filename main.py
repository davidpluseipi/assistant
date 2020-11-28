import csv
import pyautogui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import pyscreenshot as image_grabber
import pytesseract
from PySide2.QtCore import Slot, Qt
import sys
import threading
from time import sleep


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        # basic setup
        self.setGeometry(400, 400, 500, 300)
        self.label = QtWidgets.QLabel(self)

        # menu stuff
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # setup for exit
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
        self.file_menu.addAction(exit_action)

        # start a separate thread
        my_thread = threading.Thread(target=self.do_stuff)
        my_thread.start()

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    def do_stuff(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\david\AppData\Local\Tesseract-OCR\tesseract.exe'
        x_max = image_grabber.grab().size[0]
        y_max = image_grabber.grab().size[1]
        while True:
            x1, y1 = pyautogui.position()
            x2 = x1 + 400
            if x2 > x_max:
                x2 = x_max
            y2 = y1 + 300
            if y2 > y_max:
                y2 = y_max
            im = image_grabber.grab(bbox=(x1, y1, x2, y2))
            the_string = pytesseract.image_to_string(im)
            with open(r'c:\g\code\assistant\data\contacts.csv') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                a = ''  # to prevent reporting duplicates
                for row in reader:
                    given_name = row["Given Name"]
                    if given_name != '' and the_string.find(f'{given_name}') != -1 and a != given_name:
                        a = given_name
                        full_text = f'{row["Name"]}\n{row["Phone 1 - Value"]}\n{row["E-mail 1 - Value"]}'
                        self.label.setText(full_text)
                        self.label.adjustSize()
                        self.label.move(20, 50)
            sleep(0.1)
            QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui1 = Interface()
    ui1.show()
    app.exec_()

