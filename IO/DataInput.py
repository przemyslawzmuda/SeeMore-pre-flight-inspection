from Exception.InputIntMismatchException import InputIntMismatchException


class InputInt:
    def __init__(self, message: str):
        """
        :param message: Insert a message to inform the user what kind of integer value is needed.
        """
        self.message = message

    def return_input_int(self) -> int:
        try:
            value = input(self.message)
            return int(value)
        except ValueError:
            raise InputIntMismatchException(value) from None