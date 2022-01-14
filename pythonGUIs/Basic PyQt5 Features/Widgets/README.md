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

&emsp; You can combine flags together using pipes (|), however note that you can only use one vertical or horizontal alignment flag at a time.
``` align_top_left = Qt.AlignLeft | Qt.AlignTop ```

**Qt Flags** :
*Note that you use an OR pipe (|) to combine the two flags by convention. The flags are non-overlapping bitmasks. e.g. 
Qt.AlignLeft has the binary value 0b0001, while Qt.AlignBottom is 0b0100. 
By ORing together we get the value 0b0101 representing 'bottom left'.*

### Finally, there is also a shorthand flag that centers in both directions simultaneously—
| Flag | Behavior |
| --- | --- |
| Qt.AlignCenter | Centers horizontally and vertically |

&emsp; Weirdly, you can also use QLabel to display an image using the .setPixmap() method. This accepts an pixmap (a pixel array), which you can create by passing an image filename to QPixmap. \
&emsp; By default the image scales while maintaining its aspect ratio. If you want it to stretch and scale to fit the window completely you can set .setScaledContents(True) on the QLabel.
| .setScaledContents(False) | .setScaledContents(True) |
| --- | --- |
| ![True](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/images/widgets_QLabel_QPixmap_False.png) | ![False](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/images/widgets_QLabel_QPixmap_True.png) |

🚀 Run [widgets_QLabel_QPixmap.py](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/widgets_QLabel_QPixmap.py)

## QCheckBox
&emsp; You can set a checkbox state programmatically using .setChecked or .setCheckState. The former accepts either True or False representing checked or unchecked respectively. However, with .setCheckState you also specify a partially checked state using a Qt. namespace flag—
| Flag | Behavior |
| --- | --- |
| Qt.Checked | Item is checked |
| Qt.Unchecked | Item is unchecked |
| Qt.PartiallyChecked | Item is partially checked |

&emsp; If you set the value to Qt.PartiallyChecked the checkbox will become tri-state (that is have three possible states). You can also set a checkbox to be tri-state without setting the current state to partially checked by using .setTriState(True)

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

```
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

&emsp; You can add items to a QComboBox by passing a list of strings to .addItems(). Items will be added in the order they are provided. \
&emsp; QComboBox can also be editable, allowing users to enter values not currently in the list and either have them inserted, or simply used as a value. To make the box editable: ``` widget.setEditable(True) ``` \
&emsp; You can also set a flag to determine how the insert is handled. These flags are stored on the QComboBox class itself and are listed below—
| Flag | Behavior |
| --- | --- |
| QComboBox.NoInsert | No insert |
| QComboBox.InsertAtTop | Insert as first item |
| QComboBox.InsertAtCurrent | Replace currently selected item |
| QComboBox.InsertAtBottom | Insert after last item |
| QComboBox.InsertAfterCurrent | Insert after current item |
| QComboBox.InsertBeforeCurrent | Insert before current item |
| QComboBox.InsertAlphabetically | Insert in alphabetical order |

&emsp; To use these, apply the flag as follows: ``` widget.setInsertPolicy(QComboBox.InsertAlphabetically) ``` \
&emsp; You can also limit the number of items allowed in the box by using .setMaxCount, e.g. ``` widget.setMaxCount(10) ``` \

🚀 Run [widgets_QComboBox_1.py](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Widgets/widgets_QComboBox_1.py) to test it!
