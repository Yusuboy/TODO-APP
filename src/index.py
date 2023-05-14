from tkinter import Tk
from ui.ui import UI

"""
    Entry point for the Todo-APP program.

    Creates a Tkinter window, sets its title to "Todo-APP", creates a UI object, initializes it, and starts the Tkinter
    mainloop to run the UI.

"""
def main():
    window = Tk()
    window.title("Todo-APP")

    ui_view = UI(window)
    ui_view.initate()

    window.mainloop()


if __name__ == "__main__":
    main()
    