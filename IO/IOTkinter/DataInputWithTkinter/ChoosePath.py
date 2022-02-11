from tkinter import filedialog, messagebox

from Exception.PathException import NoChosenFilePathException, NoChosenDirectoryPathException

from IO.IOTkinter.ConfigureTkinterApplication import ConfigureTkinterNotification

'''
Options for message boxes with Tkinter:
showinfo, showwarning, showerror, askquestion, askokcancel, askyesno.
'''


class InputFilePathWithTkinter(ConfigureTkinterNotification, filedialog.FileDialog):

    def __init__(self, information_message):
        """
        :param information_message: Display the information message with intentions to User.
        """
        super().__init__(information_message)

    def configure_notification(self):
        messagebox.showinfo("Information", self.message)
        file_path = filedialog.askopenfilename()
        if not file_path:
            raise NoChosenFilePathException from None
        return file_path


class InputDirectoryPathWithTkinter(ConfigureTkinterNotification):
    def __init__(self, information_message):
        super().__init__(information_message)

    def configure_notification(self):
        messagebox.showinfo("Information", self.message)
        directory_path = filedialog.askdirectory()
        if directory_path == '':
            raise NoChosenDirectoryPathException from None
        return directory_path
