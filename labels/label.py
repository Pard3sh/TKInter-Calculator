import tkinter as tk


class Label:
    def __init__(self, root, font):
        self.value = tk.StringVar()
        self.value.set("")
        label = tk.Label(root, textvariable=self.value, anchor=tk.E, bg="#F5F5F5",
                     fg="#25265E", padx=24, font=font)
        label.pack(expand=True, fill="both")

    def update(self, update):
        self.value.set(update)
