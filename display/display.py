import tkinter as tk


class Display:
    def __init__(self, root):
        self.frame = tk.Frame(root, height=221, bg="white")
        self.frame.pack(expand=True, fill="both")