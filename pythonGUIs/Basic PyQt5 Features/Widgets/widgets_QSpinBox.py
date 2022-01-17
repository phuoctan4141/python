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

"""
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
"""