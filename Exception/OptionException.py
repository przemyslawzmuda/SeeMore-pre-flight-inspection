class NoSuchOptionException(Exception):
    """
    Raise the following exception in case of input value out of available range.
    """

    def __init__(self, input_choice, message_error):
        self.input_choice = input_choice
        self.message_error = message_error
        super().__init__(self.message_error)
        '''
        Override the constructor of the Exception class in order to accept my own arguments. 
        '''

    def __str__(self):  # __str__ called when an instance is printed
        return f"{self.message_error} ---> {self.input_choice}"
