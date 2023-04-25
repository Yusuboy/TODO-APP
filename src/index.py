from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Todo-APP")

    ui_view = UI(window)
    ui_view.initate()

    window.mainloop()


if __name__ == "__main__":
    main()