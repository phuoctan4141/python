# A simple Model View — a Todo List

## The UI

The simple UI was laid out using Qt Creator and saved as mainwindow.ui. The .ui file is included in the downloads for this book.

![Designing the UI in Qt Creator](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Model%20View%20Architecture/Todo%20List%20/images/Designing%20the%20UI%20in%20Qt%20Creator.png)

The widgets available in the interface were given the IDs shown in the table below.

| objectName  | Type | Description |
| --- | --- | --- |
| todoView | QListView | The list of current todos |
| todoEdit | QLineEdit | The text input for creating a new todo item |
| addButton | QPushButton | Create the new todo, adding it to the todos list |
| deleteButton | QPushButton | Delete the current selected todo, removing it from the todos list |
| completeButton | QPushButton | Mark the current selected todo as done |

## The Model

We define our custom model by subclassing from a base implementation,
allowing us to focus on the parts unique to our model. Qt provides a number
of different model bases, including lists, trees and tables (ideal for
spreadsheets)

For this example we are displaying the result to a QListView. The matching
base model for this is QAbstractListModel. The outline definition for our model
is shown below.

```python
class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)
```

The `.todos` variable is our data store. The two methods `rowcount()` and `data()` 
are standard Model methods we must implement for a list model. We’ll go
through these in turn below.

### .todos list

The data store for our model is .todos, a simple Python list in which we’ll store
a tuple of values in the format [(bool, str), (bool, str), (bool, str)] where
bool is the done state of a given entry, and str is the text of the todo.

We initialize self.todo to an empty list on startup, unless a list is passed in via
the todos keyword argument.

To create an instance of this model we can simply do —
```python
model = TodoModel() # create an empty todo list
```

Or to pass in an existing list —
```python
todos = [(False, 'an item'), (False, 'another item')]
model = TodoModel(todos)
```

### .rowcount()

The .rowcount() method is called by the view to get the number of rows in the
current data. This is required for the view to know the maximum index it can
request from the data store (row count-1). Since we’re using a Python list as
our data store, the return value for this is simply the len() of the list.

### .data()

This is the core of your model, which handles requests for data from the view
and returns the appropriate result. It receives two parameters index and role.

index is the position/coordinates of the data which the view is requesting,
accessible by two methods .row() and .column() which give the position in
each dimension. For a list view column can be ignored.

role is a flag indicating the type of data the view is requesting. This is
because the .data() method actually has more responsibility than just the
core data. It also handles requests for style information, tooltips, status bars,
etc. — basically anything that could be informed by the data itself.

The naming of Qt.DisplayRole is a bit weird, but this indicates that the view is
asking us "please give me data for display". There are other roles which the
data can receive for styling requests or requesting data in "edit-ready" format.


| Role  | Value | Description |
| --- | --- | --- |
| Qt.DisplayRole  | 0 | The key data to be rendered in the form of text. QString |
| Qt.DecorationRole | 1 | The data to be rendered as a decoration in the form of an icon. QColor, QIcon or QPixmap |
| Qt.EditRole | 2 | The data in a form suitable for editing in an editor. QString |
| Qt.ToolTipRole  | 3 | The data displayed in the item’s tooltip. QString |
| Qt.StatusTipRole | 4 | The data displayed in the status bar. QString |
| Qt.WhatsThisRole | 5 | The data displayed for the item in "What’s This?" mode. QString |
| Qt.SizeHintRole  | 13 | The size hint for the item that will be supplied to views. QSize |

For a full list of available roles that you can receive see the Qt ItemDataRole
documentation. Our todo list will only be using Qt.DisplayRole and
Qt.DecorationRole.

## Basic implementation

Below is the basic stub application needed to load the UI and display it. We’ll
add our model code and application logic to this base.

```python
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
```

We define our TodoModel as before, and initialize the MainWindow object. In the
__init__ for the MainWindow we create an instance of our todo model and
set this model on the todo_view.
Next we’ll make it possible to add items from within the
application.

```python
def add(self):
    """
    Add an item to our todo list, getting the text from the QLineEdit .todoEdit
    and then clearing it.
    """
    text = self.todoEdit.text()
    # Remove whitespace from the ends of the string.
    text = text.strip()
    if text:  # Don't add empty strings.
        # Access the list via the model.
        self.model.todos.append((False, text))
        # Trigger refresh.
        self.model.layoutChanged.emit() # (1)
        # Empty the input
        self.todoEdit.setText("")
        self.save()

(1) Here we’re emitting a model signal .layoutChanged to let the view know
that the shape of the data has been altered. This triggers a refresh of the
entirety of the view. If you omit this line, the todo will still be added but
the QListView won’t update.
```

If just the data is altered, but the number of rows/columns are unaffected
you can use the .dataChanged() signal instead. This also defines an altered
region in the data using a top-left and bottom-right location to avoid
redrawing the entire view.


## Hooking up the other actions

We can now connect the rest of the button’s signals and add helper
functions for performing the delete and complete operations. We add the
button signals to the __init__ block as before.

Then define a new delete method as follows —
```python
def delete(self):
    indexes = self.todoView.selectedIndexes()
    if indexes:
        # Indexes is a single-item list in single-select mode.
        index = indexes[0]
        # Remove the item and refresh.
        del self.model.todos[index.row()]
        self.model.layoutChanged.emit()
        # Clear the selection (as it is no longer valid).
        self.todoView.clearSelection()
        self.save()
```

We use self.todoView.selectedIndexes to get the indexes (actually a list of a
single item, as we’re in single-selection mode) and then use the .row() as an
index into our list of todos on our model. We delete the indexed item using
Python’s del operator, and then trigger a layoutChanged signal because the
shape of the data has been modified.

The complete method looks like this —
```python
def complete(self):
    indexes = self.todoView.selectedIndexes()
    if indexes:
        index = indexes[0]
        row = index.row()
        status, text = self.model.todos[row]
        self.model.todos[row] = (True, text)
        # .dataChanged takes top-left and bottom right, which are equal
        # for a single selection.
        self.model.dataChanged.emit(index, index)
        # Clear the selection (as it is no longer valid).
        self.todoView.clearSelection()
        self.save()
```

This uses the same indexing as for delete, but this time we fetch the item
from the model .todos list and then replace the status with True.

The key difference here vs. standard Qt widgets is that we make changes
directly to our data, and simply need to notify Qt that some change has
occurred — updating the widget state is handled automatically.


## Using Qt.DecorationRole

If you run the application you should now find that adding and deleting both
work, but while completing items is working, there is no indication of it in the
view. We need to update our model to provide the view with an indicator to
display when an item is complete. The updated model is shown below.

```python
tick = QtGui.QImage('tick.png')
```

We’re using a tick icon tick.png to indicate completed items, which we load
into a QImage object named tick. In the model we’ve implemented a handler
for the Qt.DecorationRole which returns the tick icon for rows who’s status is
True (for complete).



## A persistent data store

Our todo app works nicely, but it has one fatal flaw — it forgets your todos as
soon as you close the application While thinking you have nothing to do
when you do may help to contribute to short-term feelings of Zen, long term
it’s probably a bad idea.

The solution is to implement some sort of persistent data store. The simplest
approach is a simple file store, where we load items from a JSON or Pickle file
at startup and write back any changes.

To do this we define two new methods on our MainWindow class — load and
save. These load data from a JSON file name data.json (if it exists, ignoring the
error if it doesn’t) to self.model.todos and write the current self.model.todos
out to the same file, respectively

```python
def load(self):
    try:
        with open("data.json", "r") as f:
            self.model.todos = json.load(f)
    except Exception:
        pass


def save(self):
    with open("data.json", "w") as f:
        data = json.dump(self.model.todos, f)
```

To persist the changes to the data we need to add the .save() handler to the
end of any method that modifies the data, and the .load() handler to the
__init__ block after the model has been created

## The final code looks like this —

```python
import json
import os
import sys

from PyQt5.QtCore import QAbstractListModel, Qt
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow

basedir = os.path.dirname(__file__)

tick = QImage(os.path.join(basedir, "tick.png"))


class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.todoEdit.text()
        # Remove whitespace from the ends of the string.
        text = text.strip()
        if text:  # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            self.save()

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a single-item list in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()

    def load(self):
        try:
            with open("data.json", "r") as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open("data.json", "w") as f:
            data = json.dump(self.model.todos, f)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

If the data in your application has the potential to get large or more complex,
you may prefer to use an actual database to store it. Qt provides models for
interacting with SQL databases which we’ll cover shortly.
