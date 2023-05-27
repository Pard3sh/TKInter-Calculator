import tkinter as tk


class Window:
    def __init__(self, root=None):
        self.window = tk.Tk(root)

    def update_window(self):
        self.window.mainloop()
