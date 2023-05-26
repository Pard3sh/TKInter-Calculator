import tkinter as tk


class OutputLabel:
    def __init__(self, root):
        self.output = "0"
        self.label = tk.Label(root.frame, text=self.output, anchor=tk.E, bg="#F5F5F5",
                              fg="#25265E", padx=24, font=("Arial", 16))
        self.label.pack(expand=True, fill="both")

    def set_output(self, output):
        self.output = output
