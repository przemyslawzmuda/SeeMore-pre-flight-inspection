from tkinter.simpledialog import askinteger
from IO.IOTkinter.TkinterApplication import RunTkinterApplication


class AskUserForIntegerNumber(RunTkinterApplication):

    def __init__(self, message, min_value, max_value):
        super().__init__(message)
        self.min_value = min_value
        self.max_value = max_value

    def displaySomething(self) -> int:
        int_number = askinteger("Enter number", self.message, minvalue=self.min_value, maxvalue=self.max_value)
        return int_number
