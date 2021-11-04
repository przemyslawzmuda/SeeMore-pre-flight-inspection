class InputIntMismatchException(Exception):
    """
    Attributes:
        input parameter -- value not instance of int causes the error
        message -- information according to error
    """

    def __init__(self, input_parameter, message_error):
        self.input_parameter = input_parameter
        self.message_error = message_error
        super().__init__(self.message_error)
        '''
        Override the constructor of the Exception class in order to accept my own arguments. 
        '''

    def __str__(self):  # __str__ called when an instance is printed
        return f"{self.input_parameter} -> {self.message_error}"
        '''
        The following inherited __str__ method of the Exception class is used to display the message when
        the exception is raised. I can customize the __str__ by overriding that.
        '''
