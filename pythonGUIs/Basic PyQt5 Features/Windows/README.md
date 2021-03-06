# Windows
## Creating a new window
To create a new window in PyQt5 you just need to create a new instance of a widget object without a parent. This can be any widget (technically any subclass of QWidget) including another QMainWindow if you prefer. 

There is no restriction on the number of QMainWindow instances you can have, and if you need toolbars or menus on your second window you will need to use QMainWindow for that too. 

As with your main window, creating a window is not sufficient, you must also show it.

```python
import sys

from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                             QVBoxLayout, QWidget)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        w = AnotherWindow()
        w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
```

If you run this, you’ll see the main window. Clicking the button may show the second window, but if you see it it will only be visible for a fraction of a second. What’s happening?

```python
    def show_new_window(self, checked):
        w = AnotherWindow()
        w.show()
```

We are creating our second window inside this method, storing it in the variable w and showing it. However, once we leave this method the w variable will be cleaned up by Python, and the window destroyed. To fix this we need to keep a reference to the window somewhere—on the main window self object, for example.

```python
    def show_new_window(self, checked):
        self.w = AnotherWindow()
        self.w.show()
```

🚀 Run [windows_1b](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Windows/windows_1b.py)! Now, when you click the button to show the new window, it will persist.

However, what happens if you click the button again? The window will be re-created! This new window will replace the old in the self.w variable, and the previous window will be destroyed. You can see this more clearly if you change the AnotherWindow definition to show a random number in the label each time it is created.

```python
import sys

from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
```

The init block is only run when creating the window. If you keep clicking the button the number will change, showing that the window is being re-created.

One solution is to simply check whether the window has already being created before creating it. The full example below shows this in action.

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
```

This approach is fine for windows that you create temporarily, or need to change dependent on the current state of the program – for example if you want to show a particular plot, or log output. However, for many applications you have a number of standard windows that you want to be able to show/hide on demand.

In the next part we’ll look at how to work with these types of windows.

## Closing a window
As we previously saw, if no reference to a window is kept, it will be discarded (and closed). We can use this behavior to close a window, replacing the
show_new_window method from the previous example with –

```python
    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()

        else:
            self.w = None  # Discard reference, close window.
```

By setting self.w to None (or any other value) the reference to the window will be lost, and the window will close. However, if we set it to any other value
than None the first test will not pass, and we will not be able to recreate a window.

This will only work if you have not kept a reference to this window somewhere else. To make sure the window closes regardless, you may want to explicitly call .close() on it.

```python
    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()

        else:
            self.w.close()
            self.w = None  # Discard reference, close window.
```

## Persistent windows
So far we’ve looked at how to create new windows on demand. However, sometimes you have a number of standard application windows. In this case it can often make more sense to create the additional windows first, then use .show() to display them when needed.

In the following example we create our external window in the __init__ block for the main window, and then our show_new_window method simply calls self.w.show() to display it.

```python
import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
```

🚀 If you run this, clicking on the button will show the window as before. Note that the window is only created once and calling .show() on an already visible window has no effect.

## Showing & hiding windows
Once you have created a persistent window you can show and hide it without recreating it. Once hidden the window still exists, but will not be 
visible and accept mouse/other input. However you can continue to call methods on the window and update it’s state – including changing it’s
appearance. Once re-shown any changes will be visible.

Below we update our main window to create a toggle_window method whichchecks, using .isVisible() to see if the window is currently visible. If it is not, it 
is shown using .show() , if it is already visible we hide it with .hide().

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()

        else:
            self.w.show()
```

The complete working example of this persistent window and toggling the show/hide state is shown below.

```python
import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()

        else:
            self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
```

🚀 Again, the window is only created once – the window’s __init__ block is not re-run (so the number in the label does not change) each time the window is re-shown.
