import sys
import time

from IO.IOTerminal.DataInputWithTerminal.DataInput import InputInt
from EnumUserOptions import UserChoiceOptions
from Exception.OptionException import NoSuchOptionException
from IO.IOTkinter.DataOutputWithTkinter.DisplayNotifications import DisplayErrorNotification
from Exception.InputIntMismatchException import InputIntMismatchException
from Model.SeeMoreSoftware.SeeMorePreprocesing import SeeMorePreprocessingController
from Model.SeeMoreSoftware.SeeMorePreprocesing.SeeMorePreprocessing import SeeMorePreprocessingSoftware
from Model.NeuralNetorkModelsPackage.NeuralNetworkConfiguration.LearningStarter import LetTheLearnBegin


class AppController:
    def __init__(self):
        self.preprocessData = SeeMorePreprocessingController.PreprocessingController()

    def mainAppController(self):
        user_choice = None
        while user_choice != UserChoiceOptions.EXIT.value:
            self.displayOptionsToUser()
            user_choice = self.getUserOption()
            self.switchOptionInDictionaryPossibilities(user_choice)
            print("\n")

    def displayOptionsToUser(self):
        for option in UserChoiceOptions:
            print(f"{option.value} --- {option.label}")

    def getUserOption(self):
        while True:
            try:
                choice_number = InputInt("Choose available option: ").return_input_int()
                choice_enum_option = UserChoiceOptions.return_choice_option_from_values_list(choice_number)
                return choice_enum_option
            except InputIntMismatchException as error_message:
                DisplayErrorNotification(error_message).runNotification()
            except NoSuchOptionException as error_message:
                DisplayErrorNotification(error_message).runNotification()

    def switchOptionInDictionaryPossibilities(self, option):
        dictionary_options = {
            0: self.closeApp,
            1: SeeMorePreprocessingSoftware.extract_zip_file,
            2: self.preprocessData.clean_images_data_set,
            3: self.preprocessData.createTrainingValidationDataSets,
            4: LetTheLearnBegin.starter
        }
        dictionary_options[option]()

    def closeApp(self):
        print("Thank You for working with us.")
        time.sleep(2)
        print(f"Closing app", end="")
        for x in range(3):
            time.sleep(1.5)
            print(".", end="")
        sys.exit()
