import tkinter


class ConfigureTkinterNotification:

    def __init__(self, message):
        self.message = message

    def configureNotification(self):
        """
        Override that function in the child class.
        """
        pass

    def runApp(self):
        window_root = tkinter.Tk()
        window_root.withdraw()
        self.configureNotification()
        window_root.destroy()
