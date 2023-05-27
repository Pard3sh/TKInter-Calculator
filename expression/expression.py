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


    def remove(self):
        self.equation = self.equation[:len(self.equation) - 1]

    def clear(self):
        self.equation = ''
        self.expression_label.update(self.get_equation())
        self.output_label.update(self.get_equation())

    def get_equation(self):
        return self.equation

    def calculate(self):
        try:
            value = str(eval(self.equation))
            return True, value
        except:
            return False, self.equation
