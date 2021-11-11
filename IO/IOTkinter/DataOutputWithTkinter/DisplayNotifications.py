import tkinter as tk
from tkinter import messagebox


class ShowInformationToUser:
    def __init__(self, message_info):
        self.message_info = message_info

    def show_message(self):
        messagebox.showinfo("Process information", self.message_info)

    def display_notification(self):
        root = tk.Tk()
        root.withdraw()
        self.show_message()
        root.update()


class DisplayErrorNotification(ShowInformationToUser):

    def __init__(self, error_message):
        super().__init__(error_message)

    def show_message(self):
        messagebox.showwarning("Error information", self.message_info)