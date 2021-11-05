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
            self.switchOptionsDictionary(userChoice)

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

    def switchOptionsDictionary(self, option):
        dictionaryOptions = {
            0: self.closeApp,
            1: self.unzipFile,
            2: self.startCleaning,
            3: self.createDataSetsForNeuralNetwork
        }
        dictionaryOptions[option]()

    def closeApp(self):
        print("Thank You for working with us.\nClosing app...")

    def unzipFile(self):
        print("Unziping the following file.")

    def startCleaning(self):
        print("Starting process to clean images data set.")

    def createDataSetsForNeuralNetwork(self):
        print("Creating data sets for training and validation.")

c = AppController()
c.mainAppController()



