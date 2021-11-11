from tkinter import filedialog, messagebox
from IO.IOTkinter.ConfigureTkinterApplication import ConfigureTkinterNotification

'''
Options for message boxes with Tkinter:
showinfo, showwarning, showerror, askquestion, askokcancel, askyesno.
'''


class InputFilePathWithTkinter(ConfigureTkinterNotification):

    def __init__(self, information_message):
        """
        :param information_message: Display the information message with intentions to User.
        """
        super().__init__(information_message)

    def configureNotification(self):
        messagebox.showinfo("Information", self.message)
        file_path = filedialog.askopenfilename()
        return file_path


class InputDirectoryPathWithTkinter(ConfigureTkinterNotification):
    def __init__(self, information_message):
        super().__init__(information_message)

    def configureNotification(self):
        messagebox.showinfo("Information", self.message)
        directory_path = filedialog.askdirectory()
        return directory_path
