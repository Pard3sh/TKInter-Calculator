import tkinter as tk


class OutputLabel:
    def __init__(self, root):
        self.output = tk.StringVar()
        self.output.set("")
        label = tk.Label(root.frame, textvariable=self.output, anchor=tk.E, bg="#F5F5F5",
                              fg="#25265E", padx=24, font=("Arial", 16))
        label.pack(expand=True, fill="both")

    def update(self, update):
        self.output.set(update)
