# Signals & Slots

## Receiving data
&emsp; The .clicked signal is no exception, also providing a checked (or toggled) state for the button. For normal buttons this is always False, so our first slot ignored this data.

## Storing data
&emsp; Often it is useful to store the current state of a widget in a Python variable. This allows you to work with the values like any other Python variable and without accessing the original widget. You can either store these values as individual variables or use a dictionary if you prefer.
\
&emsp; You can use this same pattern with any PyQt5 widgets. If a widget does not provide a signal that sends the current state, you will need to retrieve the value from the widget directly in your handler. 

