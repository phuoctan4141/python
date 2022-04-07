# Widgets
In Qt widget is the name given to a component of the UI that the user can interact with. User interfaces are made up of multiple widgets, arranged within the window. Qt comes with a large selection of widgets available, and even allows you to create your own custom widgets.

## QLabel
### The flags available for horizontal alignment are—
| Flag | Behavior |
| --- | --- |
| Qt.AlignLeft | Aligns with the left edge. |
| Qt.AlignRight | Aligns with the right edge. |
| Qt.AlignHCenter | Centers horizontally in the available space. |
| Qt.AlignJustify | Justifies the text in the available space. |

### The flags available for vertical alignment are—
| Flag | Behavior |
| --- | --- |
| Qt.AlignTop | Aligns with the top. |
| Qt.AlignBottom | Aligns with the bottom. |
| Qt.AlignVCenter | Centers vertically in the available space. |

You can combine flags together using pipes (|), however note that you can only use one vertical or horizontal alignment flag at a time.
``` align_top_left = Qt.AlignLeft | Qt.AlignTop ```

**Qt Flags** :
*Note that you use an OR pipe (|) to combine the two flags by convention. The flags are non-overlapping bitmasks. e.g. 
Qt.AlignLeft has the binary value 0b0001, while Qt.AlignBottom is 0b0100. 
By ORing together we get the value 0b0101 representing 'bottom left'.*

### Finally, there is also a shorthand flag that centers in both directions simultaneously—
| Flag | Behavior |
| --- | --- |
| Qt.AlignCenter | Centers horizontally and vertically |

Weirdly, you can also use QLabel to display an image using the .setPixmap() method. This accepts an pixmap (a pixel array), which you can create by passing an image filename to QPixmap. 

By default the image scales while maintaining its aspect ratio. If you want it to stretch and scale to fit the window completely you can set .setScaledContents(True) on the QLabel.
| .setScaledContents(False) | .setScaledContents(True) |
| --- | --- |
| ![True](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/images/widgets_QLabel_QPixmap_False.png) | ![False](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/images/widgets_QLabel_QPixmap_True.png) |

🚀 Run [widgets_QLabel_QPixmap.py](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/widgets_QLabel_QPixmap.py)

## QCheckBox
You can set a checkbox state programmatically using .setChecked or .setCheckState. The former accepts either True or False representing checked or unchecked respectively. However, with .setCheckState you also specify a partially checked state using a Qt. namespace flag—
| Flag | Behavior |
| --- | --- |
| Qt.Checked | Item is checked |
| Qt.Unchecked | Item is unchecked |
| Qt.PartiallyChecked | Item is partially checked |

If you set the value to Qt.PartiallyChecked the checkbox will become tri-state (that is have three possible states). You can also set a checkbox to be tri-state without setting the current state to partially checked by using .setTriState(True)

**Note** : *You may notice that when the script is running the current
state number is displayed as an int with checked = 2,
unchecked = 0, and partially checked = 1. You don’t need to
remember these values, the Qt.Checked namespace variable
== 2 for example. This is the value of these state’s respective
flags. This means you can test state using state == Qt.Checked.*

| Default | Tri-State |
| --- | --- |
| ![De](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/images/widgets_QCheckBox_default.png)  | ![Tri](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/images/widgets_QCheckBox_tristate.png) |

🚀 Run [widgets_QCheckBox.py](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/widgets_QCheckBox.py)

## QComboBox
**Infor** : *You have probably seen the combo box used for selection of
font faces, or size, in word processing applications. Although
Qt actually provides a specific font-selection combo box as
QFontComboBox.*

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an int
        print(i)

    def text_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

'''
The .currentIndexChanged signal is triggered when the currently selected item
is updated, by default passing the index of the selected item in the list.
However, when connecting to the signal you can also request an alternative
version of the signal by appending [str] (think of the signal as a dict). This
alternative interface instead provides the label of the currently selected item,
which is often more useful.
'''
```

🚀 Run it! You’ll see a combo box with 3 entries. Select one and it will be shown in the box.

You can add items to a QComboBox by passing a list of strings to .addItems(). Items will be added in the order they are provided. 

QComboBox can also be editable, allowing users to enter values not currently in the list and either have them inserted, or simply used as a value. To make the box editable: ``` widget.setEditable(True) ``` 

You can also set a flag to determine how the insert is handled. These flags are stored on the QComboBox class itself and are listed below—
| Flag | Behavior |
| --- | --- |
| QComboBox.NoInsert | No insert |
| QComboBox.InsertAtTop | Insert as first item |
| QComboBox.InsertAtCurrent | Replace currently selected item |
| QComboBox.InsertAtBottom | Insert after last item |
| QComboBox.InsertAfterCurrent | Insert after current item |
| QComboBox.InsertBeforeCurrent | Insert before current item |
| QComboBox.InsertAlphabetically | Insert in alphabetical order |

To use these, apply the flag as follows: ``` widget.setInsertPolicy(QComboBox.InsertAlphabetically) ``` 

You can also limit the number of items allowed in the box by using .setMaxCount, e.g. ``` widget.setMaxCount(10) ``` 

🚀 Run [widgets_QComboBox_1.py](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/widgets_QComboBox_1.py) to test them!

## QListBox
This widget is similar to QComboBox, except options are presented as a scrollable list of items. It also supports selection of multiple items at once. A QListBox offers an currentItemChanged signal which sends the QListItem (the element of the list box), and a currentTextChanged signal which sends the text of the current item.

```python
import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])
        
        # In QListWidget there are two separate signals for the item, and the str
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! You’ll see the same three items, now in a list. The selected item (if any) is highlighted.

## QLineEdit

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        # widget.setReadOnly(True) # uncomment this to make readonly

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! You’ll see a simple text entry box, with a hint.

You can set a maximum length for the text field by using .setMaxLength. Placeholder text, which is text shown until something is entered by the user can be added using .setPlaceholderText. 

The QLineEdit has a number of signals available for different editing events including when return is pressed (by the user), when the user selection is changed. There are also two edit signals, one for when the text in the box has been edited and one for when it has been changed. The distinction here is between user edits and programmatic changes. The textEdited signal is only sent when the user edits text. 

Additionally, it is possible to perform input validation using an input mask to define which characters are supported and where. This can be applied to the field as follows: ``` widget.setInputMask('000.000.000.000;_') ``` . The above would allow a series of 3-digit numbers separated with periods, and could therefore be used to validate IPv4 addresses.

## QSpinBox and QDoubleSpinBox
QSpinBox provides a small numerical input box with arrows to increase and decrease the value. QSpinBox supports integers while the related widget QDoubleSpinBox supports floats.

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! You’ll see a numeric entry box. The value shows pre and post fix units, and is limited to the range +3 to -10.

To set the range of acceptable values you can use setMinimum and setMaximum,
or alternatively use setRange to set both simultaneously. Annotation of value
types is supported with both prefixes and suffixes that can be added to the
number, e.g. for currency markers or units using .setPrefix and .setSuffix
respectively. 

Clicking on the up and down arrows on the widget will increase or decrease
the value in the widget by an amount, which can be set using .setSingleStep.
Note that this has no effect on the values that are acceptable to the widget. 

Both QSpinBox and QDoubleSpinBox have a .valueChanged signal which fires
whenever their value is altered. The raw .valueChanged signal sends the
numeric value (either an int or a float) while the str alternate signal,
accessible via .valueChanged[str] sends the value as a string, including both
the prefix and suffix characters.

## QSlider
&emsp; There is an additional .sliderMoved signal that is triggered whenever the slider moves position and a .sliderPressed signal that emits whenever the slider is clicked.

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSlider()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! You’ll see a slider widget. Drag the slider to change the value.

You can also construct a slider with a vertical or horizontal orientation by passing the orientation in as you create it. The orientation flags are defined in
the Qt. namespace: ``` widget.QSlider(Qt.Vertical) ``` OR ``` widget.QSlider(Qt.Horizontal) ```

## QDial
The QDial is a rotatable widget that functions just like the slider, but appears as an analogue dial.

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDial, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! You’ll see a dial, rotate it to select a number from the range.

The signals are the same as for QSlider and retain the same names (e.g. .sliderMoved).
