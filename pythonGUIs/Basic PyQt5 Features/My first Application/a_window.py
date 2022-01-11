import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Change the title of the our main window
        self.setWindowTitle("My First App")
        button = QPushButton("Press Me!")
        # Setting the size on the window
        self.setFixedSize(QSize(400, 300))
        # Set the central widget of the window
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
