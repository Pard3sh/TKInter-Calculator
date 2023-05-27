from labels.label import Label


class OutputLabel(Label):
    def __init__(self, root):
        font = ("Arial", 16)
        super().__init__(root, font)
