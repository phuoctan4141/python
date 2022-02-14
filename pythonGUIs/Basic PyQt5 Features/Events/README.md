# Events
One of the main events which widgets receive is the QMouseEvent.
QMouseEvent events are created for each and every mouse movement and
button click on a widget. The following event handlers are available for
handling mouse events—
| Event handler | Event type moved |
| --- | --- |
| mouseMoveEvent | Mouse moved |
| mousePressEvent | Mouse button pressed |
| mouseReleaseEvent | Mouse button released |
| mouseDoubleClickEvent | Double click detected |

For example, clicking on a widget will cause a QMouseEvent to be sent to the
.mousePressEvent event handler on that widget. This handler can use the event
object to find out information about what happened, such as what triggered
the event and where specifically it occurred. \
You can intercept events by sub-classing and overriding the handler method
on the class. You can choose to filter, modify, or ignore events, passing them
up to the normal handler for the event by calling the parent class function
with super(). These could be added to your main window class as follows. In
each case e will receive the incoming event.

```
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! Try moving and clicking (and double-clicking) in the window and watch the events appear.

You’ll notice that mouse move events are only registered when you have the
button pressed down. You can change this by calling
self.setMouseTracking(True) on the window. You may also notice that the
press (click) and double-click events both fire when the button is pressed
down. Only the release event fires when the button is released. Typically to
register a click from a user you should watch for both the mouse down and
the release. \
Inside the event handlers you have access to an event object. This object
contains information about the event and can be used to respond differently
depending on what exactly has occurred. We’ll look at the mouse event
objects next.

## Mouse events
All mouse events in Qt are tracked with the QMouseEvent object, with
information about the event being readable from the following event
methods.
| Method | Returns |
| --- | --- |
| .button() | Specific button that trigger this event |
| .buttons() | State of all mouse buttons (OR’ed flags) |
| .globalPos() | Application-global position as a QPoint |
| .globalX() | Application-global horizontal X position |
| .globalY() | Application-global vertical Y position |
| .pos() | Widget-relative position as a QPoint integer |
| .posF() | Widget-relative position as a QPointF float |

You can use these methods within an event handler to respond to different
events differently, or ignore them completely. The positional methods
provide both global and local (widget-relative) position information as QPoint
objects, while buttons are reported using the mouse button types from the
Qt namespace. \
For example, the following allows us to respond differently to a left, right or
middle click on the window.

```
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
```

**Infor**: *On right-handed mice the left and right button positions are 
Qt.LeftButton. This means you don’t need to account for the
reversed, i.e. pressing the right-most button will return
mouse orientation in your code.*

The button identifiers are defined in the Qt namespace, as follows—
