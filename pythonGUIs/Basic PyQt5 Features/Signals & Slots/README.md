# Signals & Slots

## Receiving data
The .clicked signal is no exception, also providing a checked (or toggled) state for the button. For normal buttons this is always False, so our first slot ignored this data.

```python
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
Often it is useful to store the current state of a widget in a Python variable. This allows you to work with the values like any other Python variable and without accessing the original widget. You can either store these values as individual variables or use a dictionary if you prefer.

```python
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

You can use this same pattern with any PyQt5 widgets. If a widget does not provide a signal that sends the current state, you will need to retrieve the value from the widget directly in your handler.

```python
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

## Changing the interface
```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")  # <1>
        self.button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")  # <2>
        self.button.setEnabled(False)  # <3>

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

# <1> We need to be able to access the button in our the_button_was_clicked method, so we keep a reference to it on self.
# <2> You can change the text of a button by passing a str to .setText().
# <3> To disable a button call .setEnabled() with False.
```
🚀 Run it! If you click the button the text will change and the button will become unclickable.

In the following example we connect the .windowTitleChanged signal on the QMainWindow to a method slot the_window_title_changed. This slot also receives the new window title.
```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

window_titles = [  # <1>
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)  # <2>

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title) # <3>

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)  # <4>

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

# <1> A list of window titles we’ll select from using random.choice().
# <2> Hook up our custom slot method the_window_title_changed to the windows .windowTitleChanged signal.
# <3> Set the window title to the new title.
# <4> If the new window title equals "Something went wrong" disable the button.
```
🚀 Run it! Click the button repeatedly until the title changes to "Something went wrong" and the button will become disabled.
