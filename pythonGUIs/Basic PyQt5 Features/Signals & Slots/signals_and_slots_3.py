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
