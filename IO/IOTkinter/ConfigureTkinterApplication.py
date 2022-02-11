import tkinter


class ConfigureTkinterNotification:

    def __init__(self, message):
        self.message = message

    def configure_notification(self):
        """
        Override that function in the child class.
        """
        pass

    def run_notification(self):
        window_root = tkinter.Tk()
        window_root.withdraw()
        variable = self.configure_notification()
        window_root.destroy()
        if variable is not None:
            return variable
