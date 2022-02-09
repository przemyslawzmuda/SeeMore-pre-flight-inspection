import os
import time
import random

from IO.IOTkinter.DataInputWithTkinter.ChoosePath import InputDirectoryPathWithTkinter
from Model.SeeMoreSoftware.LetsMeetData import LetsMeetData
from Exception.InputIntMismatchException import InputIntMismatchException
from IO.IOTkinter.DataOutputWithTkinter.DisplayNotifications import ShowInformationToUser, DisplayErrorNotification
from Model.SeeMoreSoftware.SeeMorePreprocesing.SeeMorePreprocessing import SeeMorePreprocessingSoftware
from IO.IOTkinter.DataInputWithTkinter.DataInput import AskUserForIntegerNumber


class PreprocessingController:
    """
    - Pillar of OOP: Abstraction - hide away information and only give access to things that are crucial.
    """

    def __init__(self):
        self.preprocessSoftware = SeeMorePreprocessingSoftware()

    def clean_images_data_set(self):
        """
        The following function makes a process of cleaning a data set. It can works with one folder also with
        the main folder which contains subdirectories.
        """

        path_to_data_set = InputDirectoryPathWithTkinter("Choose a file with data sets in order to"
                                                         " start a cleaning process.").runNotification()

        # data_set_dictionary = { 'path1':[images1, ...], 'path2':[images2, ...], ... }
        data_set_dictionary = LetsMeetData.LetsMeetData.create_dictionary_paths_and_files(path_to_data_set)

        for key_path, value_images_names_list in data_set_dictionary.items():
            # items() returns a list containing a tuple for each key-value pair
            self.preprocessSoftware.clean_images_folder(key_path, value_images_names_list)

    def createTrainingValidationDataSets(self):
        """
        The following function creates the training and validation data sets. These data sets are crucial
        for ImageDataGenerator object and for the neural networks. User can indicate a directory where
        the default items for neural networks are stored (default data set). Subsequently, User is able to choose
        a directory where the Training and Validation data sets will be created with replicated images.
        """

        while True:
            try:
                training_data_size = AskUserForIntegerNumber("Enter the size of the training set in [%] "
                                                           "as an integer number").runNotification()
                assert (training_data_size in range(1, 100)), "Give the size of a training data set in range " \
                                                            "from 1% to 99%. - A training set shouldn\'t " \
                                                            "contains 100% of the images."
                break
            except AssertionError as err_message:
                DisplayErrorNotification(err_message).runNotification()
            except InputIntMismatchException as err_message:
                DisplayErrorNotification(err_message).runNotification()

        departue_path = InputDirectoryPathWithTkinter("Choose a directory where the default items (original data sets)"
                                                      " for neural network are stored.").runNotification()
        approach_path = InputDirectoryPathWithTkinter("Choose a directory where the Training and Validation "
                                                      "data sets will be created.").runNotification()

        # Express the training_data_size as a percentage value
        training_data_size /= 100

        # Create the Training and Validation folders
        training_directory, validation_directory = self.preprocessSoftware.create_folders_for_generators(approach_path)

        # Get a data dictionary: { 'path1':[images1, ...], 'path2':[images2, ...], ... }
        data_images_dictionary = LetsMeetData.LetsMeetData.create_dictionary_paths_and_files(departue_path)

        for key_path, valueImagesList in data_images_dictionary.items():
            sub_folder = os.path.basename(key_path)
            sub_folder_path_training = os.path.join(training_directory, sub_folder)
            sub_folder_path_validation = os.path.join(validation_directory, sub_folder)
            self.preprocessSoftware.create_new_folder(sub_folder_path_training)
            self.preprocessSoftware.create_new_folder(sub_folder_path_validation)

            '''
            Shuffle a valueImagesList, it doesn't return anything, only reorganize an existing list.
            The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
            Note: This method changes the original list, it does not return a new list.
            '''
            random.shuffle(valueImagesList)

            # Set the size of the training and validation data sets
            training_number_images = round(len(valueImagesList) * training_data_size)  # round float up into int number
            # validationNumberImages = len(valueImagesList) - training_number_images

            # Create images list for training and validation data sets
            training_images_list = valueImagesList[:training_number_images]  # [:x] - including the x-ith element
            validation_images_list = valueImagesList[training_number_images:]  # [x:] - not including the x-ith element

            # Copy files (imagesNames) into the training and validation folders
            for image in training_images_list:
                departue_path_image = os.path.join(key_path, image)
                approach_path_image = os.path.join(sub_folder_path_training, image)
                self.preprocessSoftware.copy_file(departue_path_image, approach_path_image)

            for image in validation_images_list:
                departue_path_image = os.path.join(key_path, image)
                approach_path_image = os.path.join(sub_folder_path_validation, image)
                self.preprocessSoftware.copy_file(departue_path_image, approach_path_image)

        time.sleep(2)
        ShowInformationToUser(
            "The process of creating Training and Validation data sets has "
            "been completed successfully.").runNotification()
        time.sleep(1)
        ShowInformationToUser(
            f"There are {len(training_images_list)} images in the Training data set.").runNotification()
        time.sleep(1)
        ShowInformationToUser(
            f"There are {len(validation_images_list)} images in the Validation data set.").runNotification()
