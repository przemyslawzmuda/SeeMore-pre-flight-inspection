import sys
import time

from EnumUserOptions import UserChoiceOptions

from IO.IOTerminal.DataInputWithTerminal.DataInput import InputInt
from IO.IOTkinter.DataOutputWithTkinter.DisplayNotifications import DisplayErrorNotification

from Exception.OptionException import NoSuchOptionException
from Exception.InputIntMismatchException import InputIntMismatchException

from Model.SeeMoreSoftware.SeeMorePreprocesing import SeeMorePreprocessingController
from Model.SeeMoreSoftware.SeeMorePreprocesing.SeeMorePreprocessing import SeeMorePreprocessingSoftware
from Model.NeuralNetorkModelsPackage.NeuralNetworkConfiguration.LearningStarter import LetTheLearnBegin


class AppController:
    def __init__(self):
        self.preprocess_data = SeeMorePreprocessingController.PreprocessingController()

    def main_app_controller(self):
        user_choice = None
        while user_choice != UserChoiceOptions.EXIT.value:
            self.display_options_to_user()
            user_choice = self.get_user_option()
            self.switch_option_in_dictionary_possibilities(user_choice)
            print("\n")

    def display_options_to_user(self):
        for option in UserChoiceOptions:
            print(f"{option.value} --- {option.label}")

    def get_user_option(self) -> int:
        while True:
            try:
                choice_number = InputInt("Choose available option: ").return_input_int()
                choice_enum_option = UserChoiceOptions.return_choice_option_from_values_list(choice_number)
                return choice_enum_option
            except InputIntMismatchException as error_message:
                DisplayErrorNotification(error_message).runNotification()
            except NoSuchOptionException as error_message:
                DisplayErrorNotification(error_message).runNotification()

    def switch_option_in_dictionary_possibilities(self, option: int):
        dictionary_options = {
            0: self.close_app,
            1: SeeMorePreprocessingSoftware.extract_zip_file,
            2: self.preprocess_data.clean_images_data_set,
            3: self.preprocess_data.createTrainingValidationDataSets,
            4: LetTheLearnBegin.starter
        }
        dictionary_options[option]()

    def close_app(self):
        print("Thank You for working with us.")
        time.sleep(2)
        print(f"Closing app", end="")
        for x in range(3):
            time.sleep(1.5)
            print(".", end="")
        sys.exit()
