from display.display import Display
from root_window import RootWindow


class Calculator:
    def __init__(self):
        self.window = RootWindow()
        self.display_frame = Display(self.window.get_window_object())

    def run(self):
        self.window.update_window()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
