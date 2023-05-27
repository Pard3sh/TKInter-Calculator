from buttons.buttons import create_buttons
from buttons.buttonsframe import create_button_frame
from display.display import Display
from expression.expression import Expression
from labels.expression_label import ExpressionLabel
from labels.output import OutputLabel
from root_window import RootWindow


class Calculator:
    def __init__(self):
        self.window = RootWindow()
        display_frame = Display(self.window)
        buttons_frame = create_button_frame(self.window)
        equation = Expression(display_frame)

        create_buttons(buttons_frame, equation)

    def run(self):
        self.window.update_window()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
