# My first Application

```
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Change the title of our main window
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
```

- Common Qt widgets are always imported from the QtWidgets namespace.
- Must always call the __init__ method of the super() class.
- When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.
- As well as .setFixedSize() you can also call .setMinimumSize() and .setMaximumSize() to set the minimum and maximum sizes respectively.

:rocket: Run it! You will now see your window again, but this time with the QPushButton widget in the middle. Pressing the button will do nothing, we’ll sort that next.

