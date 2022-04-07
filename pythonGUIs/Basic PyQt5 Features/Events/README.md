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
the event and where specifically it occurred. 

You can intercept events by sub-classing and overriding the handler method
on the class. You can choose to filter, modify, or ignore events, passing them
up to the normal handler for the event by calling the parent class function
with super(). These could be added to your main window class as follows. In
each case e will receive the incoming event.

```python
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
the release. 

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
Qt namespace. 

For example, the following allows us to respond differently to a left, right or
middle click on the window.

```python
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
| Identifier | Value (binary) | Represents |
| --- | --- | --- |
| Qt.NoButton | 0 (000) | No button pressed, or the event is not related to button press. |
| Qt.LeftButton | 1 (001) | The left button is pressed |
| Qt.RightButton | 2 (010) | The right button is pressed. |
| Qt.MiddleButton | 4 (100) | The middle button is pressed. |

For a more in-depth look at how this all works check out Enums & the Qt Namespace later.

## Context menus
Context menus are small context-sensitive menus which typically appear
when right clicking on a window. Qt has support for generating these
menus, and widgets have a specific event used to trigger them. In the
following example we’re going to intercept the .contextMenuEvent a
QMainWindow. This event is fired whenever a context menu is about to be
shown, and is passed a single value event of type QContextMenuEvent. 

To intercept the event, we simply override the object method with our new
method of the same name. So in this case we can create a method on our
MainWindow subclass with the name contextMenuEvent and it will receive all
events of this type.

```python
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(e.globalPos())
```

If you run the above code and right-click within the window, you’ll see a
context menu appear. You can set up .triggered slots on your menu actions
as normal (and re-use actions defined for menus and toolbars).

When passing the initial position to the exec_ function, this
this case we pass self as the parent, so we can use the global
must be relative to the parent passed in while defining. In
position. 

Just for completeness, there is actually a signal-based approach to creating context menus.

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(self.mapToGlobal(pos))
```

🚀 Run and It’s entirely up to you which you choose.

## Event hierarchy
In pyqt5 every widget is part of two distinct hierarchies: the Python object
hierarchy, and the Qt layout hierarchy. How you respond or ignore events can
affect how your UI behaves.

## Python inheritance forwarding
Often you may want to intercept an event, do something with it, yet still
trigger the default event handling behavior. If your object is inherited from a
standard widget, it will likely have sensible behavior implemented by default.
You can trigger this by calling up to the parent implementation using
super(). 

This is the Python parent class, not the pyqt5 .parent().

```python
def mousePressEvent(self, event):
  print("Mouse pressed!")
  super(self, MainWindow).contextMenuEvent(event)
````

The event will continue to behave as normal, yet you’ve added some non-interfering behavior.

## Layout forwarding
When you add a widget to your application, it also gets another parent from
the layout. The parent of a widget can be found by calling .parent().
Sometimes you specify these parents manually, such as for QMenu or QDialog,
often it is automatic. When you add a widget to your main window for
example, the main window will become the widget’s parent. 

When events are created for user interaction with the UI, these events are
passed to the uppermost widget in the UI. So, if you have a button on a
window, and click the button, the button will receive the event first. 

The the first widget cannot handle the event, or chooses not to, the event will
bubble up to the parent widget, which will be given a turn. This bubbling
continues all the way up nested widgets, until the event is handled or it
reaches the main window. 

In your own event handlers you can choose to mark an event as handled
calling .accept()—

```python
  class CustomButton(Qbutton)
    def mousePressEvent(self, e):
        e.accept()
```

Alternatively, you can mark it as unhandled by calling .ignore() on the event
object. In this case the event will continue to bubble up the hierarchy.

```python
  class CustomButton(Qbutton)
    def event(self, e):
        e.accept()
```

If you want your widget to appear transparent to events, you can safely
ignore events which you’ve actually responded to in some way. Similarly, you
can choose to accept events you are not responding to in order to silence
them.
