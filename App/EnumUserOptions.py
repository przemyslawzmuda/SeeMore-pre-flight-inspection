from enum import Enum, unique

from Exception.OptionException import NoSuchOptionException


@unique
class UserChoiceOptions(Enum):
    """The following Enum class stores the available options for users that could be perform by the application."""

    # __new__() -> must be used whenever you want to customize the actual value of the Enum member.
    # For example, if you want to pass several items to the constructor, but only one of them to be the value.
    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj

    # NAME (.name) = VALUE (.value), LABEL(.label)
    EXIT = (0, "Exit.")
    OPEN_ZIP_DATA = (1, "Unzip the zip file.")
    CLEAN_DATA_SETS = (2, "Start cleaning process of the images.")
    CREATE_DATA_SETS_FOR_NEURAL_NETWORK = (3, "Create subdirectories for the training and validation data sets.")
    START_LEARNING = (4, "Start deep learning process.")

    '''
    The @unique decorator searches an enumeration's __members__ gathering any aliases it finds. If any are found
    ValueError is raised with details. If there isn't @unique decorator, will not be any information about duplications.
    '''

    @staticmethod
    def return_choice_option_from_values_list(option_choice: int) -> int:
        try:
            choice_options_number = [option.value for option in UserChoiceOptions]
            return choice_options_number[option_choice]
        except IndexError:
            raise NoSuchOptionException(option_choice, "No available option:")
        except TypeError as error_message:
            print(error_message)
