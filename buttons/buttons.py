# this will be the widget that contains all of the operations
import tkinter as tk


class Buttons:
    def __init__(self, root):
        self.frame = tk.Frame(root.window)
        self.frame.pack(expand=True, fill="both")

