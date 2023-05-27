from buttons import *
from display.display import create_display
from expression.expression import Expression

from root_window import RootWindow


class Calculator:
    def __init__(self):
        self.window = RootWindow()
        display_frame = create_display(self.window)
        equation = Expression(display_frame)
        b_frame = buttons_frame.create_button_frame(self.window)

        buttons.create_buttons(b_frame, equation)

    def run(self):
        self.window.update_window()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
