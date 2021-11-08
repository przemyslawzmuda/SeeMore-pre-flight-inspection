import tkinter as tk
from tkinter import filedialog, messagebox


class InputFilePathWithTkinter:
    def __init__(self, information_message):
        """
        :param information_message: Display the information message with intentions to User.
        """
        self.information_message = information_message

    '''
    Options for message boxes with Tkinter:
    showinfo, showwarning, showerror, askquestion, askokcancel, askyesno.
    '''

    def show_info_message(self):
        messagebox.showinfo("Information", self.information_message)

    def return_file_path(self):
        root = tk.Tk()
        root.withdraw()
        self.show_info_message()
        file_path = filedialog.askopenfilename()
        return file_path
