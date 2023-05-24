import tkinter as tk
from ..window.window import Window


class Display(Window):
    def __init__(self, root):
        super(Display, self).__init__(root=root)
        self.window.geometry(str(root.winfo_width()) + "x" + str(int(root.winfo_height() * .2)))
