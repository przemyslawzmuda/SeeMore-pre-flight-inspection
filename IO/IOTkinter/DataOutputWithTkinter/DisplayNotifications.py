from tkinter import messagebox

from IO.IOTkinter.ConfigureTkinterApplication import ConfigureTkinterNotification


class ShowInformationToUser(ConfigureTkinterNotification):

    def __init__(self, message_info):
        super().__init__(message_info)

    def configure_notification(self):
        messagebox.showinfo("Process information", self.message)


class DisplayErrorNotification(ConfigureTkinterNotification):

    def __init__(self, error_message):
        super().__init__(error_message)

    def configure_notification(self):
        messagebox.showwarning("Error information", self.message)


class BreakWorkingLoopFunction(ConfigureTkinterNotification):
    def __init__(self, message):
        super().__init__(message)

    def configure_notification(self):
        return messagebox.askyesno(title="confirmation", message=self.message)
