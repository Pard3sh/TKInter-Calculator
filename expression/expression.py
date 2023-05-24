# will be the thing that contains the equation

class Expression:
    def __init__(self):
        self.equation = ''

    def append(self, char):
        self.equation += char

    def remove(self):
        self.equation = self.equation[:len(self.equation) - 1]

    def clear(self):
        self.equation = ''

    def get_equation(self):
        return self.equation

    def calculate(self):
        try:
            value = str(eval(self.equation))
            return True, value
        except:
            return False, self.equation
