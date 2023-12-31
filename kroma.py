import tkinter
from tkinter import ttk
from tkinter import messagebox

class Align():

    # === Attributes ===
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

class Anchor():

    # === Attributes ===
    CENTER = "center"
    TOP = "n"
    TOP_RIGHT = "ne"
    TOP_LEFT = "nw"
    BOTTOM = "s"
    BOTTOM_RIGHT = "se"
    BOTTOM_LEFT = "sw"
    RIGHT = "e"
    LEFT = "w"

class State():

    # === Attributes ===
    NORMAL = "normal"
    MINIMIZED = "iconic"
    MAXIMIZED = "zoomed"
    HIDDEN = "withdrawn"

class MessageBoxType():

    # === Attributes ===
    INFORMATION = 0
    WARNING = 1
    ERROR = 2
    QUESTION = 3

class MessageBox():

    # === MAIN methods ===

    @staticmethod
    def Show(message : str, type=MessageBoxType.INFORMATION, title="Message Box") -> bool:
        """ It shows a message box. Returns true if it succeeds or if the 'Yes' option was chosen (Question message box). """

        match (type):
            case MessageBoxType.QUESTION:
                return True if (messagebox.askyesno(title, message)) else False

            case MessageBoxType.ERROR:
                messagebox.showerror(title, message)
                return True

            case MessageBoxType.WARNING:
                messagebox.showwarning(title, message)
                return True
            
            case _:
                messagebox.showinfo(title, message)
                return True


class Window():

    def __init__(self) -> None:

        # === Attributes ===
        self.__id = tkinter.Tk()
        self.__icon = None
        self.__title = "Window"
        self.__resizable = None
        self.__size = [800, 600]
        self.__state = State.NORMAL
        self.__shaking = False
        self.__screen = [self.__id.winfo_screenwidth(), self.__id.winfo_screenheight()]
        self.__position = [int(self.__screen[0] / 2) - int(self.__size[0] / 2), int(self.__screen[1] / 2) - int(self.__size[1] / 2)]

    # === MAIN methods ===

    def Create(self):
        """ Creates and runs the window. """
        self.__id.title(self.__title)
        self.__id.geometry(f"{self.__size[0]}x{self.__size[1]}+{int(self.__position[0])}+{int(self.__position[1])}")
        self.__id.iconbitmap(self.__icon)
        self.__id.state(self.__state)

        if (not self.__resizable):
            self.__id.resizable(width=self.__resizable, height=self.__resizable)
        
        # Runs the window
        self.__id.mainloop()

    def Close(self):
        """ Closes the window. """
        self.__id.destroy()

    def Shake(self):
        """ Shakes the window. """
        self.__shaking = True

        AMOUNT = 2
        TIME = 10

        if (self.__shaking):
            for i in range(TIME):
                self.__id.geometry(f"+{self.__id.winfo_x() + AMOUNT}+{self.__id.winfo_y()}")
                self.__id.update()
                self.__id.after(TIME)

                self.__id.geometry(f"+{self.__id.winfo_x() - AMOUNT}+{self.__id.winfo_y()}")
                self.__id.update()
                self.__id.after(TIME)

        self.__shaking = False
        
    # === GET methods ===

    def GetId(self):
        """ Gets the window's id. """
        return self.__id
    
    def GetIcon(self) -> str:
        """ Gets the window's icon. """
        return self.__icon

    def GetTitle(self) -> str:
        """ Gets the window's title. """
        return self.__title

    def GetSize(self) -> list:
        """ Gets the window's size. """
        return self.__size

    def GetScreen(self) -> list:
        """ Gets the screen's size in pixels. """
        return self.__screen

    def GetState(self) -> str:
        """ Gets the window's state. """
        return self.__state

    def GetPosition(self) -> list:
        """ Gets the window's position in pixels. """
        return self.__position

    # === SET methods ===

    def SetIcon(self, icon : str):
        """ Sets the window's icon. """
        self.__icon = icon

    def SetTitle(self, title : str):
        """ Sets the window's title. """
        self.__title = title

    def SetResizable(self, resizable : bool):
        """ Sets the window's resizable. """
        self.__resizable = resizable

    def SetSize(self, width : int, height : int):
        """ Sets the window's size. """
        self.__size = [width, height]
        self.__position = [int(self.__screen[0] / 2) - int(self.__size[0] / 2), int(self.__screen[1] / 2) - int(self.__size[1] / 2)]

    def SetState(self, state : State):
        """ Sets the window's state. """
        self.__state = state

    def SetPosition(self, width : int, height : int):
        """ Sets the window's position. """
        self.__position = [width, height]

class Widget():

    def __init__(self) -> None:

        # === Attributes ===

        # • Data
        self._id = None
        self._root = None

        # • Appearance
        self._color = "black"
        self._backgroundColor = "white"

        # • Behavior
        self._enabled = True
        # self._visible = True (Work in progress)
        self._focused = False

        # • Layout
        self._anchor = Anchor.TOP_LEFT
        self._padding = [0, 0]
        self._position = [0, 0]
        self._size = [12, 1]

    # === GET methods ===

    # • Data
    def GetId(self):
        """ Gets the widget's id. """
        return self._id
    
    def GetRoot(self):
        """ Gets the widget's root. """
        return self._root
    
    # • Appearance
    def GetColor(self) -> str:
        return self._color
    
    def GetBackgroundColor(self) -> str:
        return self._backgroundColor

    # • Behavior
    def GetFocus(self) -> bool:
        return self._focused
    
    # • Layout
    def GetAnchor(self) -> str:
        """ Gets the widget's anchor. """
        return self._anchor
    
    def GetPosition(self) -> list:
        """ Gets the widget's position in pixels. """
        return self._position
    
    def GetSize(self) -> list:
        """ Gets the widget's size in pixels. """
        return self._size

    # === SET methods ===

    # • Data
    def SetRoot(self, root):
        """ Sets the widget's root. """
        self._root = root

    # • Appearance
    def SetColor(self, color: str):
        self._color = color
    
    def SetBackgroundColor(self, backgroundColor: str):
        self._backgroundColor = backgroundColor

    # • Behavior
    def SetFocus(self, enable: bool):
        """ Focus the widget. """
        self._focused = enable

    # • Layout
    def SetAnchor(self, anchor: Anchor):
        """ Sets the widget's anchor. """

        match (anchor):
            case Anchor.CENTER:
                self._anchor = anchor
                self._padding = [0.5, 0.5]

            case Anchor.TOP:
                self._anchor = anchor
                self._padding = [0.5, 0.0]

            case Anchor.TOP_RIGHT:
                self._anchor = anchor
                self._padding = [1.0, 0.0]

            case Anchor.TOP_LEFT:
                self._anchor = anchor
                self._padding = [0.0, 0.0]

            case Anchor.BOTTOM:
                self._anchor = anchor
                self._padding = [0.5, 1.0]

            case Anchor.BOTTOM_RIGHT:
                self._anchor = anchor
                self._padding = [1.0, 1.0]

            case Anchor.BOTTOM_LEFT:
                self._anchor = anchor
                self._padding = [0.0, 1.0]

            case Anchor.RIGHT:
                self._anchor = anchor
                self._padding = [1.0, 0.5]

            case Anchor.LEFT:
                self._anchor = anchor
                self._padding = [0.0, 0.5]

    def SetPosition(self, x: int, y: int):
        """ Sets the widget's position in pixels. """
        self._position = [x, y]

    def SetSize(self, width: int, height: int):
        """ Sets the widget's size in pixels. """
        self._size = [width, height]

class Form():

    def __init__(self) -> None:
        # === Attributes ===
        self.__window = None
        self.__widgets = None

    # === MAIN methods ===

    def Initialize(self):
        super().__init__()
        self.__window = Window()
        self.__widgets = []

    def CreateSubobject(self, subobject):
        self.__widgets.append(subobject)
        widget = subobject
        widget.SetRoot(self.__window)
        return widget

    def Run(self):

        # Creates all the form's subojects
        for i in range(len(self.__widgets)):
            self.__widgets[i].Create()

        # Creates the form's window
        self.__window.Create()

    # === GET methods ===

    def GetWindow(self) -> Window:
        """ Gets the current form's window. """
        return self.__window

class Button(Widget):

    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===
        self.__event = None
        self.__text = "Button"

    # === MAIN methods ===

    def Create(self):
        """ Creates the button. """
        self._id = tkinter.Button(self._root.GetId() if (self._root != None) else self._root, text=self.__text, command=self.__event)
        self._id.config(width=self._size[0], height=self._size[1], fg=self._color, bg=self._backgroundColor, border=0)

        # Set button's focus
        if (self._focused):
            self._id.focus()

        # Set button's hover and leave effect
        self._id.bind("<Enter>", func=lambda e: self._id.config(cursor="hand2"))
        self._id.bind("<Leave>", func=lambda e: self._id.config(cursor="arrow"))

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])
            
    # === SET methods ===

    def SetEvent(self, event):
        """ Sets the button's event. """
        self.__event = event

    def SetText(self, text: str):
        """ Sets the button's text. """
        self.__text = text

        if (self._id != None):
            self._id.config(text=self.__text)

class Label(Widget):
    
    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===
        self.__text = "Label"
        self._size = [0, 0]
        self._backgroundColor = None

    # === MAIN methods ===

    def Create(self):
        """ Creates the label. """
        self._id = tkinter.Label(self._root.GetId() if (self._root != None) else self._root, text=self.__text)
        self._id.config(width=self._size[0], height=self._size[1], fg=self._color, bg=self._backgroundColor)

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    # === GET methods ===

    def GetText(self) -> str:
        """ Sets the label's text. """
        return self.__text
    
    # === SET methods ===

    def SetText(self, text: str):
        """ Sets the label's text. """
        self.__text = text

        if (self._id != None):
            self._id.config(text=self.__text)

class ComboBox(Widget):

    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===
        self.__content = ["Combo Box"]
        self.__readonly = "readonly"
        self._size = [12, 0]

    # === MAIN methods ===

    def Create(self):
        """ Creates the combo box. """
        self._id = ttk.Combobox(self._root.GetId() if (self._root != None) else self._root, values=self.__content)
        self._id.config(width=self._size[0], height=self._size[1], state=self.__readonly)

        # Sets the first combo box's element as default value
        self._id.set(self.__content[0])

        # Set button's focus
        if (self._focused):
            self._id.focus()

        # Set button's hover and leave effect
        self._id.bind("<Enter>", func=lambda e: self._id.config(cursor="hand2"))
        self._id.bind("<Leave>", func=lambda e: self._id.config(cursor="arrow"))

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    # === GET methods ===

    def GetContent(self) -> str:
        """ Gets the combo box's content. """
        return self._id.get() if (self._id.get() != "Combo Box") else ""

    # === SET methods ===

    def SetContent(self, content : list):
        """ Sets the combo box's content. """
        self.__content = content

    def SetReadOnly(self, readonly : bool):
        """ Sets the combo box's state """
        self.__readonly = "readonly" if (readonly) else "normal"


class InputBox(Widget):

    def __init__(self) -> None:
        super().__init__()

    # === MAIN methods ===

    def Clear(self):
        """ Clears the input box's content. """
        self._id.delete(0, "end")

    # === GET methods ===

    def GetContent(self) -> str:
        """ Gets the input box's content. """
        return self._id.get() if (self._placeholderMode) else ""
    
    # === SET methods ===

    def SetContent(self, text : str):
        """ Sets the input box's content. """
        if (self._id != None):
            self._id.insert(0, text)

class TextBox(InputBox):
    
    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===
        self.__alignment = Align.LEFT
        self.__character = None
        self._placeholderMode = False
        self._placeholderText = None
        self._placeholderColor = None

    # === MAIN methods ===

    def _OnFocusIn(self, *args):
        """ Set-up the begin of the focus event. """
        if (self._id["fg"] == self._placeholderColor):
            self._placeholderMode = True
            self._id.delete(0, "end")
            self._id["fg"] = self._color
            self._id.config(show=self.__character)

    def _OnFocusOut(self, *args):
        """ Set-up the end of the focus event. """
        if (not self._id.get()):
            self._placeholderMode = False
            self._id.insert(0, self._placeholderText)
            self._id["fg"] = self._placeholderColor
            self._id.config(show="")

    def Create(self):
        """ Creates the text box. """
        self._id = tkinter.Entry(self._root.GetId() if (self._root != None) else self._root)
        self._id.config(justify=self.__alignment, width=self._size[0], fg=self._color, bg=self._backgroundColor, border=0)

        # Set text box's placeholder
        if (self._placeholderText != None):
            self._id.bind("<FocusIn>", self._OnFocusIn)
            self._id.bind("<FocusOut>", self._OnFocusOut)
            self._id.insert(0, self._placeholderText)
            self._id["fg"] = self._placeholderColor

        # Set text box's focus
        if (self._focused):
            self._id.focus()

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    # === SET methods ===

    def SetAlignment(self, align : Align):
        """ Sets the text box's alignment. """
        self.__alignment = align

    def SetPasswordCharacter(self, character):
        """ Sets the entry box's password character. """
        self.__character = character

    def SetPlaceholder(self, text : str, color="gray"):
        """ Sets the input box's placeholder. """
        if (text != ""):
            self._placeholderText = text
            self._placeholderColor = color

class RichTextBox(InputBox):
    
    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===
        self._size = [20, 10]

    # === MAIN methods ===

    def Create(self):
        """ Creates the rich text box. """
        self._id = tkinter.Text(self._root.GetId() if (self._root != None) else self._root)
        self._id.config(width=self._size[0], height=self._size[1], border=0)

        # Set rich text box's focus
        if (self._focused):
            self._id.focus()

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])
