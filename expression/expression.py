# will be the thing that contains the equation
from labels.expression_label import ExpressionLabel
from labels.output import OutputLabel


class Expression:
    def __init__(self, display_frame):
        self.equation = ''
        self.output_label = OutputLabel(display_frame)
        self.expression_label = ExpressionLabel(display_frame)

    def append(self, char):
        self.equation += char
        self.expression_label.update(self.get_equation())
        calc, val = self.is_calculateable()
        if calc:
            self.output_label.update(val)

    def remove(self):
        self.equation = self.equation[:len(self.equation) - 1]

    def clear(self):
        self.equation = ''
        self.expression_label.update(self.get_equation())
        self.output_label.update(self.get_equation())

    def get_equation(self):
        return self.equation

    def is_calculateable(self):
        self.equation = self.equation.replace("\u00F7", "/")
        self.equation = self.equation.replace("\u00D7", "*")
        try:
            value = str(eval(self.equation))
            return True, value
        except:
            return False, None

    def calculate(self):
        # "/": "\u00F7", "*": "\u00D7"
        self.equation = self.equation.replace("\u00F7", "/")
        self.equation = self.equation.replace("\u00D7", "*")
        try:
            value = str(eval(self.equation))
            self.output_label.update(value)
            self.expression_label.update(value)
            self.equation = value
        except:
            self.output_label.update("error")
