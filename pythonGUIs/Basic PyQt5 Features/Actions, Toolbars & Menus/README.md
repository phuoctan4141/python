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

&emsp; Let’s make the toolbar a bit more interesting. We could just add a QButton widget, but there is a better approach in Qt that gets you some cool features — and that is via QAction. QAction is a class that provides a way to describe abstract user interfaces. \
&emsp; Without QAction you would have to define this in multiple places. But with QAction you can define a single QAction, defining the triggered action, and
then add this action to both the menu and the toolbar. Each QAction has names, status messages, icons and signals that you can connect to (and much more).

```
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

'''
Why is the signal always false?
The signal passed indicates whether the action is checked,
and since our button is not checkable — just clickable — it is
always false. This is just like the QPushButton we saw earlier.
'''
```

&emsp; To start with we create the function that will accept the signal from the QAction so we can see if it is working. Next we define the QAction itself. When
creating the instance we can pass a label for the action and/or an icon. You must also pass in any QObject to act as the parent for the action — here we’re
passing self as a reference to our main window. Strangely for QAction the parent element is passed in as the final parameter. \
&emsp;  Next, we can opt to set a status tip — this text will be displayed on the status bar once we have one. Finally we connect the .triggered signal to the custom
function. This signal will fire whenever the QAction is 'triggered' (or activated).

Let’s add a statusbar. \
&emsp; We create a status bar object by calling QStatusBar and passing the result into .setStatusBar. Since we don’t need to change the statusBar settings we can
just pass it in as we create it. We can create and define the status bar in a single line:

```
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! Hover your mouse over the toolbar button and you will see the status text appear in the status bar at the bottom of the window.

&emsp; Next we’re going to turn our QAction toggleable — so clicking will turn it on, clicking again will turn it off. To do this, we simple call .setCheckable(True) on
the QAction object.

```
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! Click on the button to see it toggle from checked to unchecked state. Note that custom slot function we create now alternates outputting True and False.

***There is also a .toggled signal, which only emits a signal when
the button is toggled. But the effect is identical so it is mostly
pointless.***

&emsp; You also need to let the toolbar know how large your icons are, otherwise your icon will be surrounded by a lot of padding. You can do this by calling
.setIconSize() with a QSize object.

```
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("bug.png"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! The QAction is now represented by an icon. Everything should function exactly as it did before.

