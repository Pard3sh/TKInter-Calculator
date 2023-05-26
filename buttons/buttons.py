import tkinter as tk


def create_buttons(root):
    clear_button(root)
    equal_button(root)
    num_buttons(root)
    operator_buttons(root)


def clear_button(root):
    button = tk.Button(root, text="C", bg="#F8FAFF", fg="#25265E", font=("Arial", 20), borderwidth=0)
    button.grid(row=0, column=1, sticky=tk.NSEW, columnspan=3)


def equal_button(root):
    button = tk.Button(root, text="=", bg="#CCEDFF", fg="#25265E", font=("Arial", 20), borderwidth=0)
    button.grid(row=4, column=3, sticky=tk.NSEW, columnspan=2)


def operator_buttons(root):
    i = 0
    operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
    for operator, symbol in operations.items():
        button = tk.Button(root, text=symbol, bg="#F8FAFF", fg="#25265E", font=("Arial", 20), borderwidth=0)
        button.grid(row=i, column=4, sticky=tk.NSEW)
        i += 1


def num_buttons(root):
    nums = {  # contains the numbers and their values
        1: (3, 1), 2: (3, 2), 3: (3, 3),
        4: (2, 1), 5: (2, 2), 6: (2, 3),
        7: (1, 1), 8: (1, 2), 9: (1, 3),
        0: (4, 2), '.': (4, 1)
    }
    for num, grid_value in nums.items():
        button = tk.Button(root, text=str(num), bg="#FFFFFF", fg="#25265E", font=("Arial", 24), borderwidth=0)
        button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
