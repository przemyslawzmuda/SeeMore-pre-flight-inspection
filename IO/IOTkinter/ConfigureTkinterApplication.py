import tkinter
from tkinter import filedialog, messagebox


class ConfigureTkinterNotification:

    def __init__(self, message):
        self.message = message

    def configureNotification(self):
        """
        Override that function in the child class.
        """
        pass

    def runNotification(self):
        window_root = tkinter.Tk()
        window_root.withdraw()
        variable = self.configureNotification()
        window_root.destroy()
        if variable is not None:
            return variable
