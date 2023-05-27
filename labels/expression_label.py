import tkinter as tk


class ExpressionLabel:
    def __init__(self, root):
        self.equation = tk.StringVar()
        self.equation.set("")

        self.label = tk.Label(root.frame, textvariable=self.equation, anchor=tk.E, bg="#F5F5F5",
                              fg="#25265E", padx=24, font=("Arial", 40, "bold"))
        self.label.pack(expand=True, fill="both")

    def update(self, update):
        self.equation.set(update)

