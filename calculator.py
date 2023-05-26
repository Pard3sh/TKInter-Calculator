from buttons.buttons import create_buttons
from buttons.buttonsframe import create_button_frame
from display.display import Display
from labels.expression import ExpressionLabel
from labels.output import OutputLabel
from root_window import RootWindow


class Calculator:
    def __init__(self):
        self.window = RootWindow()
        self.display_frame = Display(self.window)
        self.buttons_frame = create_button_frame(self.window)
        create_buttons(self.buttons_frame)
        self.output_label = OutputLabel(self.display_frame)
        self.expression_label = ExpressionLabel(self.display_frame)
        self.button_frame = 0

    def run(self):
        self.window.update_window()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
