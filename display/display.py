import tkinter as tk


class Display:
    def __int__(self, root):
        self.window = tk.Tk()
        self.window.winfo_width()
        self.window.geometry(str(root.winfo_width()) + "x" + str(int(root.winfo_height() * .2)))
