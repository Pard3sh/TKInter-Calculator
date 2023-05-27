from labels.label import Label


class ExpressionLabel(Label):
    def __init__(self, root):
        font = ("Arial", 40, "bold")
        super().__init__(root, font)


