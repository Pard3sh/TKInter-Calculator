import tkinter as tk


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        photo = tk.PhotoImage(file="resources/calculator_icon.png")
        self.window.iconphoto(False, photo)
        self.window.config(bg='#121212')
        self.update_window()

    def update_window(self):
        self.window.mainloop()
