# Signals & Slots

## Receiving data
&emsp; The .clicked signal is no exception, also providing a checked (or toggled) state for the button. For normal buttons this is always False, so our first slot ignored this data.

```
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")
    
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```
🚀 Run it! If you press the button you’ll see it highlighted as checked.
    Press it again to release it. Look for the check state in the console.
    
## Storing data
&emsp; Often it is useful to store the current state of a widget in a Python variable. This allows you to work with the values like any other Python variable and without accessing the original widget. You can either store these values as individual variables or use a dictionary if you prefer.
```
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True # <1>

        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked) # <2>

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked # <3>
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

# <1> Set the default value for our variable.
# <2> Use the default value to set the initial state of the widget.
# <3> When the widget state changes, update the variable to match.
```  
\
&emsp; You can use this same pattern with any PyQt5 widgets. If a widget does not provide a signal that sends the current state, you will need to retrieve the value from the widget directly in your handler.
```
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!") # <1>
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released) # <2>
        self.button.setChecked(self.button_is_checked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked() # <3>

        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

# <1> We need to keep a reference to the button on self so we can access it in our slot.
# <2> The released signal fires when the button is released, but does not send the check state.
# <3> .isChecked() returns the check state of the button.
```
