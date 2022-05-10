from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Keysmith")
    window.geometry('1000x1000+0+0')

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
