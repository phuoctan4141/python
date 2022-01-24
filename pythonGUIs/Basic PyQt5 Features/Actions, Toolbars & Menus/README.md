# Actions, Toolbars & Menus
## Toolbars
&emsp; Qt toolbars support display of icons, text, and can also contain any standard Qt widget. However, for buttons the best approach is to make use of the QAction system to place buttons on the toolbar. \
&emsp; In Qt toolbars are created from the QToolBar class. To start you create an instance of the class and then call .addToolbar on the QMainWindow. Passing a string in as the first parameter to QToolBar sets the toolbar’s name, which will be used to identify the toolbar in the UI.

```
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! You’ll see a thin grey bar at the top of the window. This is your toolbar. Right click and click the name to toggle it off.
