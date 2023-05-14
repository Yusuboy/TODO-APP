from tkinter import Tk
from ui.ui import UI


def main():
    """
    This is the entry point for the Todo-APP program. 
    It creates a Tkinter window titled "Todo-APP", 
    initializes and runs a UI object using the Tkinter mainloop.

    """
    window = Tk()
    window.title("Todo-APP")

    ui_view = UI(window)
    ui_view.initate()

    window.mainloop()


if __name__ == "__main__":
    main()
    