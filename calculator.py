from buttons.buttons import Buttons
from display.display import Display
from labels.expression import ExpressionLabel
from labels.output import OutputLabel
from root_window import RootWindow


class Calculator:
    def __init__(self):
        self.window = RootWindow()
        self.display_frame = Display(self.window)
        self.buttons_frame = Buttons(self.window)
        self.output_label = OutputLabel(self.display_frame)
        self.expression_label = ExpressionLabel(self.display_frame)
        self.button_frame = 0

    def run(self):
        self.window.update_window()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
