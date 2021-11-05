from IO.DataInput import InputInt
from EnumUserOptions import UserChoiceOptions
from Exception.InputIntMismatchException import InputIntMismatchException


class AppController:

    def mainAppController(self):
        self.displayOptionsToUser()
        userChoice = self.inputUserChoice()

    def displayOptionsToUser(self):
        for option in UserChoiceOptions:
            print(f"{option.value} --- {option.label}")

    def inputUserChoice(self):
        while True:
            try:
                choiceNumber = InputInt("Choose available option: ").return_input_int()
                return choiceNumber
            except InputIntMismatchException as error_message:
                print(error_message)
