import os
import time
import random
from IO.DataInput import InputInt
from IO.ChoosePath import InputDirectoryPathWithTkinter
from Model.SeeMoreSoftware.LetsMeetData import LetsMeetData
from Exception.InputIntMismatchException import InputIntMismatchException
from IO.DisplayNotifications import ShowInformationToUser, DisplayErrorNotification
from Model.SeeMoreSoftware.SeeMorePreprocesing.SeeMorePreprocessing import SeeMorePreprocessingSoftware


class PreprocessingController:

    def __init__(self):
        self.preprocessSoftware = SeeMorePreprocessingSoftware()

    def cleanImagesDataSet(self):
        """
        The following function makes a process of cleaning a data set. It can works with one folder also with
        the main folder which contains subdirectories.
        """

        path_to_data_set = InputDirectoryPathWithTkinter("Choose a file with data sets in order to"
                                                         " start a cleaning process.").return_directory_path()

        # dataSetDictionary = { 'path1':[images1, ...], 'path2':[images2, ...], ... }
        dataSetDictionary = LetsMeetData.createDictionaryPathsAndFiles(path_to_data_set)

        for keyPath, valueImagesNamesList in dataSetDictionary.items():
            # items() returns a list containing a tuple for each key-value pair
            self.preprocessSoftware.cleanImagesFolder(keyPath, valueImagesNamesList)

    def createTrainingValidationDataSets(self):
        """
        The following function creates the training and validation data sets. These data sets are crucial
        for ImageDataGenerator object and for the neural networks. User can indicate a directory where
        the default items for neural networks are stored (default data set). Subsequently, User is able to choose
        a directory where the Training and Validation data sets will be created with replicated images.
        """

        while True:
            try:
                trainingDataSize = InputInt("Enter the size of the training set in [%] as an "
                                            "integer number: ").return_input_int()
                assert (trainingDataSize in range(1, 100)), "Give the size of a training data set in range " \
                                                            "from 1% to 99%. - A training set shouldn\'t " \
                                                            "contains 100% of the images."
                break
            except AssertionError as err_message:
                DisplayErrorNotification(err_message).display_notification()
            except InputIntMismatchException as err_message:
                DisplayErrorNotification(err_message).display_notification()

        departue_path = InputDirectoryPathWithTkinter("Choose a directory where the default items (original data sets)"
                                                      " for neural network are stored.").return_directory_path()
        approach_path = InputDirectoryPathWithTkinter("Choose a directory where the Training and Validation "
                                                      "data sets will be created.").return_directory_path()

        # Express the trainingDataSize as a percentage value
        trainingDataSize /= 100

        # Create the Training and Validation folders
        trainingDirectory, validationDirectory = self.preprocessSoftware.createFoldersForGenerators(approach_path)

        # Get a data dictionary: { 'path1':[images1, ...], 'path2':[images2, ...], ... }
        dataImagesDictionary = LetsMeetData.createDictionaryPathsAndFiles(departue_path)

        for keyPath, valueImagesList in dataImagesDictionary.items():
            sub_folder = os.path.basename(keyPath)
            sub_folder_path_training = os.path.join(trainingDirectory, sub_folder)
            sub_folder_path_validation = os.path.join(validationDirectory, sub_folder)
            self.preprocessSoftware.createNewFolder(sub_folder_path_training)
            self.preprocessSoftware.createNewFolder(sub_folder_path_validation)

            '''
            Shuffle a valueImagesList, it doesn't return anything, only reorganize an existing list.
            The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
            Note: This method changes the original list, it does not return a new list.
            '''
            random.shuffle(valueImagesList)

            # Set the size of the training and validation data sets
            trainingNumberImages = round(len(valueImagesList) * trainingDataSize)  # round float up into int number
            # validationNumberImages = len(valueImagesList) - trainingNumberImages

            # Create images list for training and validation data sets
            trainingImagesList = valueImagesList[:trainingNumberImages]  # [:x] - including the x-ith element
            validationImagesList = valueImagesList[trainingNumberImages:]  # [x:] - not including the x-ith element

            # Copy files (imagesNames) into the training and validation folders
            for image in trainingImagesList:
                departue_path_image = os.path.join(keyPath, image)
                approach_path_image = os.path.join(sub_folder_path_training, image)
                self.preprocessSoftware.copyFile(departue_path_image, approach_path_image)

            for image in validationImagesList:
                departue_path_image = os.path.join(keyPath, image)
                approach_path_image = os.path.join(sub_folder_path_validation, image)
                self.preprocessSoftware.copyFile(departue_path_image, approach_path_image)

        time.sleep(2)
        ShowInformationToUser(
            "The process of creating Training and Validation data sets has "
            "been completed successfully.").display_notification()
        time.sleep(1)
        ShowInformationToUser(
            f"There are {len(trainingImagesList)} images in the Training data set.").display_notification()
        time.sleep(1)
        ShowInformationToUser(
            f"There are {len(validationImagesList)} images in the Validation data set.").display_notification()
