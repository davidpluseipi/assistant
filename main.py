import csv
import pyautogui
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QLineEdit,
                             QPushButton)
import pyscreenshot as image_grabber
import pytesseract
from queue import Queue
import sys
import threading
from time import sleep
import webbrowser

global que


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        # basic setup
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle('Alfred')

        # textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        self.textbox.returnPressed.connect(self.on_click)

        # button next to textbox
        self.button1 = QPushButton('Enter', self)
        self.button1.move(320, 20)
        self.button1.clicked.connect(self.on_click)

        # label, aka title, for the contact info
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('Contact Info')
        self.label1.adjustSize()
        self.label1.move(20, 75)

        # label (as a place to put the contact info)
        self.label2 = QtWidgets.QLabel(self)

        # start a separate thread
        my_thread = threading.Thread(target=self.do_stuff, daemon=True)
        my_thread.start()

        # button to call contact
        self.button2 = QPushButton('Call', self)
        self.button2.move(320, 75)
        self.button2.clicked.connect(self.call_contact)

    @pyqtSlot()
    def on_click(self):
        textbox_value = self.textbox.text()
        print(textbox_value)
        self.textbox.setText('')

    @pyqtSlot()
    def call_contact(self):
        print(que.get())
        link = r'https://messages.google.com/web/u/0/calls/new'
        webbrowser.open_new(link)

    def do_stuff(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\david\AppData\Local\Tesseract-OCR\tesseract.exe'
        screen = image_grabber.grab()
        x_max, y_max = screen.size
        while True:
            x1, y1 = pyautogui.position()
            x2 = x1 + 200
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
                        que.put(row["Phone 1 - Value"])
                        full_text = f'{row["Name"]}\n{row["Phone 1 - Value"]}\n{row["E-mail 1 - Value"]}'
                        self.label2.setText(full_text)
                        self.label2.adjustSize()
                        self.label2.move(20, 100)
            sleep(0.1)


if __name__ == '__main__':
    que = Queue()
    app = QApplication(sys.argv)
    ui1 = Interface()
    ui1.show()
    sys.exit(app.exec_())

