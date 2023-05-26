import tkinter as tk


def create_button_frame(root):
    frame = tk.Frame(root.window)
    frame.rowconfigure(0, weight=1)
    for x in range(1, 5):
        frame.rowconfigure(x, weight=1)
        frame.columnconfigure(x, weight=1)
    frame.pack(expand=True, fill="both")
    return frame

