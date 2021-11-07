import tkinter as tk
from tkinter import filedialog


class InputFilePath:

    @staticmethod
    def return_file_path():
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path
