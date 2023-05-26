from expression.expression import Expression
import tkinter as tk


class ExpressionLabel:
    def __init__(self, root):
        self.expression = Expression()
        self.label = tk.Label(root.frame, text=self.expression.get_equation(), anchor=tk.E, bg="#F5F5F5",
                              fg="#25265E", padx=24, font=("Arial", 40, "bold"))
        self.label.pack(expand=True, fill="both")


