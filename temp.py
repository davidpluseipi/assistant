from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def update():
    label.setText("Updated")


def retrieve():
    print(label.text())


app = QApplication(sys.argv)  # this line starts the application
win = QMainWindow()  # this line actually creates the main window for the widgets
x_coord = 400  # coordinates of top left corner of window on startup
y_coord = 400
width = 500
height = 300
win.setGeometry(x_coord, y_coord, width, height)  # customize the window parameters/geometry
win.setWindowTitle('My Window Title')
# Insert bulk of code for GUI here

# Labels
label = QtWidgets.QLabel(win)
label.setText("This is a QLabel")
label.adjustSize()  # adjust the label size from the tiny default with adjustSize() to autosize
label.move(100, 100)  # move is just a basic demo. PyQt5 comes with actual layouts.

# Buttons
button = QtWidgets.QPushButton(win)
button.clicked.connect(update)
button.setText('update')
button.move(100, 150)

button2 = QtWidgets.QPushButton(win)
button2.clicked.connect(retrieve)
button2.setText('retrieve')
button2.move(100, 200)

# End bulk of code for GUI
win.show()
sys.exit(app.exec_())
