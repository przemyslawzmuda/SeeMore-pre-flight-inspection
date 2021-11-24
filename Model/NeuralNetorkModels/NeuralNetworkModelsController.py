from TestModel import TestModel
from Model.Generator.BasicDataGenerator import BasicZoomGenerator
from Model.Generator.FeedGenerator import FeedDataGenerator
from IO.IOTkinter.DataInputWithTkinter.ChoosePath import InputDirectoryPathWithTkinter
from IO.IOTkinter.DataOutputWithTkinter.DisplayNotifications import DisplayErrorNotification
from tensorflow.keras.activations import relu, softmax
from tensorflow.keras.optimizers import Adam
from ModelConfiguration import ModelConfiguration
from Model.SeeMoreSoftware.DrawConlusionsFromDeepLearning.DrawConclusions import DrawConclusionsController


class ConfigureAndRunLearningProcess:
    """
    The following class is used to read data set's directories, configure objects in order to perform
    data augmentations, configure objects in order to generate data batches as well as configure
    neural network's models and subsequently plot in the figure the values of the learning process.
    """

    def __init__(self):
        # Create an object needed to plot the values of the learning process
        self.drawConclusions = DrawConclusionsController()

    def readDirectoriesForLearning(self) -> tuple:
        path_to_training_data = InputDirectoryPathWithTkinter(
            "Choose a directory contains training data").runNotification()
        path_to_validation_data = InputDirectoryPathWithTkinter(
            "Choose a directory contains validation data").runNotification()

        # Use the tuple() constructor to make a tuple
        return tuple((path_to_training_data, path_to_validation_data))

    def configureDataAugmentations(self) -> tuple:
        try:
            # Configure a generator for the training data set - get an ImageDataGenerator object
            training_data_augmentation = BasicZoomGenerator(1./255, [0.1, 0.3]).create_zoom_generator()

            # Configure a generator for the validation data set - get an ImageDataGenerator object
            validation_data_augmentation = BasicZoomGenerator(1./255, [0.1, 0.3]).create_zoom_generator()

            # Use the tuple() constructor to make a tuple
            return tuple((training_data_augmentation, validation_data_augmentation))
        except:
            raise

    def createDataBatchesForLearning(self, path_to_training_data, training_data_augmentation, path_to_validation_data,
                                     validation_data_augmentation) -> tuple:
        try:
            # Load a training data in from directories into the training generator, turning it into the batches
            training_data_generator = FeedDataGenerator(
                path_to_training_data, 100, 10, "categorical").injectDataIntoGenerator(training_data_augmentation)

            # Load a validation data in from directories into the validation generator, turning it into the batches
            validation_data_generator = FeedDataGenerator(
                path_to_validation_data, 100, 10, "categorical").injectDataIntoGenerator(validation_data_augmentation)

            # Use a tuple constructor to make a tuple
            return tuple((training_data_generator, validation_data_generator))
        except:
            raise

    def compileAndFitNeuralNetworkModel(self, training_data_generator, validation_data_generator) -> object:
        try:
            # Return a hierarchical structure of the neural network
            artificial_neural_network_model = TestModel(relu, 3, softmax).pfi_model_0()

            # Compile the neural network model
            model_configuration_object = ModelConfiguration(
                Adam, "categorical_crossentropy", training_data_generator, 3, validation_data_generator)
            model_configuration_object.compileModel(artificial_neural_network_model)

            # Fit the neural network model subsequently start the learning process
            history_test = model_configuration_object.createHistoryAndRunModel(artificial_neural_network_model)

            return history_test
        except:
            raise

    def plotAccuracyAndLossValues(self, history_test):
        try:
            # Plot the accuracy and the cost function for training history learning as well as validation history learning
            self.drawConclusions.plotLossAccuracyGraph(history_test)
        except:
            raise
