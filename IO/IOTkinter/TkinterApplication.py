import tkinter


class RunTkinterApplication:
    def __init__(self, message):
        self.message = message

    def displayInformation(self):
        pass

    def runApp(self):
        window_root = tkinter.Tk()
        window_root.withdraw()
        self.displaySomething()
        window_root.destroy()
