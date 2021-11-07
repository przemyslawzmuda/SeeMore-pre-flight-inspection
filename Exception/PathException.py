class NoSuchDirectoryException(Exception):
    """
    Raise the following exception where there is no give directory.
    """

    def __init__(self, input_directory: str):
        self.input_directory = input_directory

    def __str__(self) -> str:
        return f"The following directory ---> {self.input_directory} not exists.\nPlease, enter the correct directory."
