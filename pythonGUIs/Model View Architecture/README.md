# Model View Architecture

## The Model View Architecture — Model View Controller

Model–View–Controller (MVC) is an architectural pattern used for developing
user interfaces. It divides an application into three interconnected parts,
separating the internal representation of data from how it is presented to
and accepted from the user.

The MVC pattern splits the interface into the following components —

* **Model** holds the data structure which the app is working with.
* **View** is any representation of information as shown to the user, whether graphical or tables. Multiple views of the same data are allowed.
* **Controller** accepts input from the user, transforms it into commands and applies these to the model or view.

In Qt land the distinction between the View & Controller gets a little murky.
Qt accepts input events from the user via the OS and delegates these to the
widgets (Controller) to handle. However, widgets also handle presentation of
their own state to the user, putting them squarely in the View. Rather than
agonize over where to draw the line, in Qt-speak the View and Controller are
instead merged together creating a Model/ViewController architecture —
called "Model View" for simplicity.

![Comparing the MVC model and the Qt ModelView](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Model%20View%20Architecture/images/Comparing%20the%20MVC%20model%20and%20the%20Qt%20ModelView%20architecture.png)

Importantly, the distinction between the data and how it is presented is
preserved.

## The Model View

The Model acts as the interface between the data store and the
ViewController. The Model holds the data (or a reference to it) and presents
this data through a standardized API which Views then consume and
present to the user. Multiple Views can share the same data, presenting it in
completely different ways.

You can use any "data store" for your model, including for example a
standard Python list or dictionary, or a database (via Qt itself, or SQLAlchemy)
— it’s entirely up to you.

The two parts are essentially responsible for —

1. The model stores the data, or a reference to it and returns individual or
ranges of records, and associated metadata or display instructions.
2. The view requests data from the model and displays what is returned on
the widget.

There is a good introduction to the Qt Model/View architecture [Model/View Programming](https://doc.qt.io/qt-5/model-view-programming.html)





