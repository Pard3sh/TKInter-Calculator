import tkinter as tk
from window.window import Window


class RootWindow(Window):
    def __init__(self):
        super(RootWindow, self).__init__()
        self.window.title("Calculator")
        photo = tk.PhotoImage(file="resources/calculator_icon.png")
        self.window.iconphoto(False, photo)
        self.window.config(bg='#121212')
        self.update_window()


