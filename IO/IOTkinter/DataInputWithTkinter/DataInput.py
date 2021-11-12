from tkinter.simpledialog import askinteger
from IO.IOTkinter.ConfigureTkinterApplication import ConfigureTkinterNotification


class AskUserForIntegerNumber(ConfigureTkinterNotification):

    def __init__(self, message):
        super().__init__(message)

    def configureNotification(self) -> int:
        int_number = askinteger("Enter number", self.message)
        return int_number
