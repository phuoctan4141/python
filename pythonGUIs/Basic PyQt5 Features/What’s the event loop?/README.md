# What’s the event loop?
![The event loop in Qt](https://github.com/phuoctan4141/python/blob/main/pythonGUIs/Basic%20PyQt5%20Features/What%E2%80%99s%20the%20event%20loop%3F/images/The%20event%20loop%20in%20Qt.png)

Each interaction with your application — whether a press of a key, click of a mouse, or mouse movement — generates an event which is placed on the event queue. In the event loop, the queue is checked on each iteration and if a waiting event is found, the event and control is passed to the specific event handler for the event. The event handler deals with the event, then passes control back to the event loop to wait for more events. There is only **one** running event loop per application.
