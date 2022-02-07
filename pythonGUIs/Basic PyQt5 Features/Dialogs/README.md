# Dialogs
In Qt dialog boxes are handled by the QDialog class. To create a new dialog
box simply create a new object of QDialog type passing in a parent widget, e.g.
QMainWindow, as its parent. \
Let’s create our own QDialog. We’ll start with a simple skeleton app with a
button to press hooked up to a slot method.

```
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("?")
        dlg.exec_()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

In the slot button_clicked (which receives the signal from the button press) we
create the dialog instance, passing our QMainWindow instance as a parent. This
will make the dialog a modal window of QMainWindow. This means the dialog
will completely block interaction with the parent window.

🚀 Run [dialogs_1.py](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/dialogs_1.py)! Click the button and you’ll see an empty dialog appear.

Once we have created the dialog, we start it using .exec_() - just like we did
for QApplication to create the main event loop of our application. That’s not a
coincidence: when you exec the QDialog an entirely new event loop - specific
for the dialog - is created. \
**One event loop to rule them all**: *Remember I said there can only be one Qt event loop running at any time? I meant it! The QDialog completely blocks your application execution. Don’t start a dialog and expect anything else to happen anywhere else in your app. We’ll see later how you can use multithreading to get you out of this pickle.* \
Like our very first window, this isn’t very interesting. Let’s fix that by adding a dialog title and a set of OK and Cancel buttons to allow the user to accept or reject the modal. \
To customize the QDialog we can subclass it.

```
class CustomDialog(QDialog):
    def __init__(self, parent=None):  # <1>
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
```

In the above code, we first create our subclass of QDialog which we’ve called
CustomDialog. As for the QMainWindow we customize it within the __init__ block
to ensure that our customizations are created as the object is created. First
we set a title for the QDialog using .setWindowTitle(), exactly the same as we
did for our main window. \
The next block of code is concerned with creating and displaying the dialog
buttons. This is probably a bit more involved than you were expecting.
However, this is due to Qt’s flexibility in handling dialog button positioning
on different platforms. \
**Easy way out?**: *You could of course choose to ignore this and use a standard
QButton in a layout, but the approach outlined here ensures
that your dialog respects the host desktop standards (OK on
left vs. right for example). Messing around with these
behaviors can be incredibly annoying to your users, so I
wouldn’t recommend it.* \
The first step in creating a dialog button box is to define the buttons want to
show, using namespace attributes from QDialogButtonBox. The full list of
buttons available is below:
| Button types |
| --- |
QDialogButtonBox.Ok
QDialogButtonBox.Open
QDialogButtonBox.Save
QDialogButtonBox.Cancel
QDialogButtonBox.Close
QDialogButtonBox.Discard
QDialogButtonBox.Apply
QDialogButtonBox.Reset
QDialogButtonBox.RestoreDefaults
QDialogButtonBox.Help
QDialogButtonBox.SaveAll
QDialogButtonBox.Yes
QDialogButtonBox.YesToAll
QDialogButtonBox.No
QDialogButtonBox.NoToAll
QDialogButtonBox.Abort
QDialogButtonBox.Retry
QDialogButtonBox.Ignore
QDialogButtonBox.NoButton
| --- |

These should be sufficient to create any dialog box you can think of. You can
construct a line of multiple buttons by OR-ing them together using a pipe (|).
Qt will handle the order automatically, according to platform standards. For
example, to show an OK and a Cancel button we used:
``` buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel ``` \
The variable buttons now contains an integer value representing those two
buttons. Next, we must create the QDialogButtonBox instance to hold the
buttons. The flag for the buttons to display is passed in as the first parameter. \
To make the buttons have any effect, you must connect the correct
QDialogButtonBox signals to the slots on the dialog. In our case we’ve
connected the .accepted and .rejected signals from the QDialogButtonBox to
the handlers for .accept() and .reject() on our subclass of QDialog. \
Lastly, to make the QDialogButtonBox appear in our dialog box we must add it
to the dialog layout. So, as for the main window we create a layout, and add
our QDialogButtonBox to it (QDialogButtonBox is a widget), and then set that
layout on our dialog. \
Finally, we launch the CustomDialog in our MainWindow.button_clicked slot.

```
    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")
```

🚀 Run [dialogs_2b](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/dialogs_2b.py)! Click to launch the dialog and you will see a dialog box with buttons in it.

## Simple message dialogs with QMessageBox
&emsp; There are many dialogs which follow the simple pattern we just saw—a message with buttons with which you can accept or cancel the dialog. While you can construct these dialogs yourself, Qt also provides a built-in message dialog class called QMessageBox. This can be used to create information, warning, about or question dialogs. \
The example below creates a simple QMessageBox and shows it.

```
    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec_()

        if button == QMessageBox.Ok:
            print("OK!")
```

🚀 Run [dialogs_3](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/dialogs_3.py)! You’ll see a simple dialog with an OK button.

&emsp; As with the dialog button box we looked at already, the buttons shown on a QMessageBox are also configured with a set of constants which can be combined with | to show multiple buttons. The full list of available button types is shown below:
| Button types |
| --- |
QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Discard
QMessageBox.Apply
QMessageBox.Reset
QMessageBox.RestoreDefaults
QMessageBox.Help
QMessageBox.SaveAll
QMessageBox.Yes
QMessageBox.YesToAll
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore
QMessageBox.NoButton
| --- |

&emsp; You can also tweak the icon shown on the dialog by setting the icon with one of the following:
|Icon state | Description |
| --- | --- |
| QMessageBox.NoIcon | The message box does not have an icon. |
| QMessageBox.Question | The message is asking a question. |
| QMessageBox.Information | The message is informational only. |
| QMessageBox.Warning | The message is warning. |
| QMessageBox.Critical | The message indicates a critical problem. |

&emsp; For example, the following creates a question dialog with Yes and No buttons.

```
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton


class MainWindow(QMainWindow):
    # end::MainWindow[]
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    # tag::button_clicked[]

    # __init__ skipped for clarity
    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a question dialog")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec_()

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")

    # end::button_clicked[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

🚀 Run it! You’ll see a question dialog with Yes and No buttons.

## Built in QMessageBox dialogs
&emsp; To make things even simpler the QMessageBox has a number of methods which can be used to construct these types of message dialog. These methods are shown below—

```
QMessageBox.about(parent, title, message)
QMessageBox.critical(parent, title, message)
QMessageBox.information(parent, title, message)
QMessageBox.question(parent, title, message)
QMessageBox.warning(parent, title, message)
```

&emsp; The parent parameter is the window which the dialog will be a child of. If you’re launching your dialog from your main window, you can just pass in self. The following example creates a question dialog, as before, with Yes and No buttons.

```
    def button_clicked(self, s):

        button = QMessageBox.question(self, "Question dialog", "The longer message")

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")
```

🚀 Run [dialogs_5](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/dialogs_5.py)! You’ll see the same result, this time using the built in .question() method.

&emsp; Notice that rather than call exec() we now simply call the dialog method and the dialog is created. The return value of each of the methods is the button which was pressed. We can detect what has been pressed by comparing the return value to the button constants. \
&emsp; The four information, question, warning and critical methods also accept optional buttons and defaultButton arguments which can be used to tweak the buttons shown on the dialog and select one by default. Generally though you don’t want to change this from the default.

```
    def button_clicked(self, s):

        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")
```

🚀 Run [dialogs_6](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/dialogs_6.py)! You’ll see a critical dialog with customized buttons.

## 🖐 Dialogs
&emsp; It’s particularly easy to create bad dialogs. From dialogs that trap users
with confusing options to nested never-ending popups. There are
plenty of ways to hurt your users.

![Some examples of bad dialogs](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/images/Some%20examples%20of%20bad%20dialogs.png)

&emsp; Dialog buttons are defined by system standards. You may never have
noticed that the OK & Cancel buttons are in different locations on
macOS & Linux vs. Windows, but your brain did. If you do not follow
system standards, you’ll confuse your users, and make them make
mistakes.

![Dialog button order is platform dependent](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/images/Dialog%20button%20order%20is%20platform%20dependent.png)

&emsp; With Qt you get this consistency for free when using the built-in
QDialogButtonBox controls. But you must use them! \
&emsp; Error dialogs annoy users. When you show an error dialog you’re giving
your users bad news. When you give someone bad news, you need to
consider the impact it will have on them. \
&emsp; Take for example this (thankfully imaginary) dialog produced when we
encounter an error in a document. The dialog tells you there is a error,
but neither what the consequences are or what to do about it. Reading
this your users will ask (possibly scream) "…and now what?" \

![An example of a bad error dialog](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/images/An%20example%20of%20a%20bad%20error%20dialog.png)

This real dialog from Acrobat Reader DC is better. This explains that
there is an error, what the consequences may be, and potentially how
to resolve it.

![Adobe Acrobat Reader DC dialog](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/images/Adobe%20Acrobat%20Reader%20DC%20dialog.png)

&emsp; But this still isn’t perfect. The error is shown as an information dialog,
which doesn’t suggest anything is wrong. The error is fired on every
page, and can appear multiple times in a document—a warning dialog
should be fired only once. The error could also be improved by making
it clear that the error is permanent.

![An improved version of the Adobe Acrobat Reader DC dialog](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/Dialogs/images/An%20improved%20version%20of%20the%20Adobe%20Acrobat%20Reader%20DC%20dialog.png)

💡 Good error messages should explain.
[ ] What happened
[ ] What was affected
[ ] What are the consequences of it
[ ] What can be done about it
