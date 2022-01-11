# My first Application

```
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")
        button = QPushButton("Press Me!")
        # Setting the size on the window
        self.setFixedSize(QSize(400, 300))
        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

- Common Qt widgets are always imported from the QtWidgets namespace.
- Must always call the __init__ method of the super() class.
- When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.

