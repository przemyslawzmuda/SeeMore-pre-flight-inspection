from enum import Enum, unique
from Exception.OptionException import NoSuchOptionException


@unique
class UserChoiceOptions(Enum):
    """
    The following enumeration class displays the optionals options for users that could be done by the application.
    """

    '''
    __new__() must be used whenever you want to customize the actual value of the Enum member.
    For example, if you want to pass several items to the constructor, but only want one of them to be the value.
    '''
    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj

    # NAME (.name) = VALUE (.value), LABEL(.label)
    EXIT = (0, "Exit.")
    OPEN_ZIP_DATA = (1, "Unzip the zip file.")
    CLEAN_DATA_SETS = (2, "Start cleaning process of the data images.")
    CREATE_DATA_SETS_FOR_NEURAL_NETWORK = (3, "Create subdirectories for training and validation data sets.")

    '''
    @unique decorator searches an enumeration's __members__ gathering any aliases it finds. If any are found
    ValueError is raised with details. I no @unique, the will not be any information about duplications.
    '''

    @staticmethod
    def createListChoiceOptions(optionChoice):
        try:
            choiceOptionsNumber = [option.value for option in UserChoiceOptions]
            return choiceOptionsNumber[optionChoice]
        except IndexError:
            raise NoSuchOptionException(optionChoice, "No available option:")
        except TypeError as error_message:
            print(error_message)

print(UserChoiceOptions.createListChoiceOptions("1111"))