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
| Qt.AlignCenter Centers | horizontally and vertically |
