import tkinter as tk


def create_buttons(root, equation):
    clear_button(root, equation)
    equal_button(root, equation)
    num_buttons(root, equation)
    operator_buttons(root, equation)


def clear_button(root, equation):
    button = tk.Button(root, text="C", bg="#F8FAFF", fg="#25265E", font=("Arial", 20),
                       borderwidth=0, command=lambda: equation.clear())
    button.grid(row=0, column=1, sticky=tk.NSEW, columnspan=3)


def equal_button(root, equation):
    button = tk.Button(root, text="=", bg="#CCEDFF", fg="#25265E",
                       font=("Arial", 20), borderwidth=0, command=lambda: equation.calculate())
    button.grid(row=4, column=3, sticky=tk.NSEW, columnspan=2)


def operator_buttons(root, equation):
    i = 0
    operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
    for operator, symbol in operations.items():
        button = tk.Button(root, text=symbol, bg="#F8FAFF", fg="#25265E",
                           font=("Arial", 20), borderwidth=0, command=lambda val=symbol: equation.append(str(val)))
        button.grid(row=i, column=4, sticky=tk.NSEW)
        i += 1


def num_buttons(root, equation):
    nums = {  # contains the numbers and their values
        1: (3, 1), 2: (3, 2), 3: (3, 3),
        4: (2, 1), 5: (2, 2), 6: (2, 3),
        7: (1, 1), 8: (1, 2), 9: (1, 3),
        0: (4, 2), '.': (4, 1)
    }
    for num, grid_value in nums.items():
        button = tk.Button(root, text=str(num), bg="#FFFFFF", fg="#25265E",
                           font=("Arial", 24), borderwidth=0, command=lambda digit=num: equation.append(str(digit)))
        button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
