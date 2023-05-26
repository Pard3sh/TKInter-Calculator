import tkinter as tk


class RootWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("365x667")
        self.window.resizable(False, False)
        photo = tk.PhotoImage(file="resources/calculator_icon.png")
        self.window.iconphoto(False, photo)
        self.window.config(bg='#121212')

    def update_window(self):
        self.window.mainloop()
