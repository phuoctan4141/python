# Layouts

There are 4 basic layouts available in Qt, which are listed in the following table.
| Layout | Behavior |
| --- | --- |
| QHBoxLayout | Linear horizontal layout |
| QVBoxLayout | Linear vertical layout |
| QGridLayout | In indexable grid XxY |
| QStackedLayout | Stacked (z) in front of one another |

There are three 2-dimensional layouts available in Qt. The QVBoxLayout, QHBoxLayout and QGridLayout. In addition there is also QStackedLayout which allows you to place widgets one on top of the other within the same space, yet showing only one layout at a time.

You can actually design and lay out your interface graphically using the Qt Designer, which we will cover later. Here we’re using code, as it’s simpler to understand and experiment with the underlying system.

## Placeholder widget

```
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
```

&emsp; In this code we subclass QWidget to create our own custom widget Color. We
accept a single parameter when creating the widget — color (a str). We first
set .setAutoFillBackground to True to tell the widget to automatically fill it’s
background with the window color. Next we change the widget’s
QPalette.Window color to a new QColor described by the value color we passed
in. Finally we apply this palette back to the widget. The end result is a widget
that is filled with a solid color, that we specify when we create it.

🚀 Run [layout_1.py](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Layouts/layout_1.py)! The window will appear, filled completely with the color red. Notice how the widget expands to fill all the available space.

## QVBoxLayout vertically arranged widgets

&emsp; With QVBoxLayout you arrange widgets one above the other linearly. Adding a widget adds it to the bottom of the column.

![A QVBoxLayout, filled from top to bottom](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Layouts/images/A%20QVBoxLayout%2C%20filled%20from%20top%20to%20bottom.png)

&emsp; Lets add our widget to a layout. Note that in order to add a layout to the QMainWindow we need to apply it to a dummy QWidget. This allows us to then use .setCentralWidget to apply the widget (and the layout) to the window. Our colored widgets will arrange themselves in the layout, contained within the QWidget in the window.

```
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! Three Color widgets arranged vertically in a QVBoxLayout. Notice the border now visible around the widget.

## QHBoxLayout horizontally arranged widgets
&emsp; QHBoxLayout is the same, except moving horizontally. Adding a widget adds it to the right hand side.

![ A QHBoxLayout, filled from left to right](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Layouts/images/A%20QHBoxLayout%2C%20filled%20from%20left%20to%20right.png)

&emsp; To use it we can simply change the QVBoxLayout to a QHBoxLayout. The boxes now flow left to right.

🚀 Run [layout_QHBoxLayout](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Layouts/layout_QHBoxLayout.py)! The widgets should arrange themselves horizontally.

## Nesting layouts
&emsp; For more complex layouts you can nest layouts inside one another using
.addLayout on a layout. Below we add a QVBoxLayout into the main QHBoxLayout.
If we add some widgets to the QVBoxLayout, they’ll be arranged vertically in the
first slot of the parent layout. \
&emsp; You can set the spacing around the layout using .setContentMargins or set the
spacing between elements using .setSpacing. 
```
layout1.setContentsMargins(0,0,0,0)
layout1.setSpacing(20)
```

| without spacing and margins around the widgets | with spacing and margins around the widgets |
| :---: | :---: |
| ![Nested QHBoxLayout and QVBoxLayout layouts](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Layouts/images/Nested%20QHBoxLayout%20and%20QVBoxLayout%20layouts.png) | ![Nested QHBoxLayout and QVBoxLayout layouts with spacing and margins](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Layouts/images/Nested%20QHBoxLayout%20and%20QVBoxLayout%20layouts%20with%20spacing%20and%20margins.png) |

🚀 Run [layout_Nesting](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Layouts/layout_Nesting.py)!

## QGridLayout widgets arranged in a grid
&emsp; QGridLayout allows you to position items specifically in a grid. You specify row
and column positions for each widget. You can skip elements, and they will
be left empty.

```
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run  it! You should see the widgets arranged in a grid, aligned despite missing entries.

