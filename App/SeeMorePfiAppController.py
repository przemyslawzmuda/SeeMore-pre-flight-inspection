from IO.DataInput import InputInt
from EnumUserOptions import UserChoiceOptions
from Exception.InputIntMismatchException import InputIntMismatchException
from Exception.OptionException import NoSuchOptionException


class AppController:

    def mainAppController(self):
        userChoice = None
        while userChoice != UserChoiceOptions.EXIT.value:
            self.displayOptionsToUser()
            userChoice = self.getUserOption()
            print(userChoice)

    def displayOptionsToUser(self):
        for option in UserChoiceOptions:
            print(f"{option.value} --- {option.label}")

    def getUserOption(self):
        while True:
            try:
                choiceNumber = InputInt("Choose available option: ").return_input_int()
                choiceEnumOption = UserChoiceOptions.returnChoiceOptionFromValuesList(choiceNumber)
                return choiceEnumOption
            except InputIntMismatchException as error_message:
                print(error_message)
            except NoSuchOptionException as error_message:
                print(error_message)

c = AppController()
c.mainAppController()