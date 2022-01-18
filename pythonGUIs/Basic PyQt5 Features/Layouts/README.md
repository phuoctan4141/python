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
