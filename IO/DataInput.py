from Exception.InputIntMismatchException import InputIntMismatchException


class DataInput:

    @staticmethod
    def input_int(number: int):
        try:
            return int(number)
        except ValueError:
            raise InputIntMismatchException(number) from None
