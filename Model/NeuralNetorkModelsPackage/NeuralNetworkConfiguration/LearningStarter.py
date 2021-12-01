from NeuralNetworkModelsController import ConfigureAndRunLearningProcess
from IO.IOTkinter.DataOutputWithTkinter.DisplayNotifications import ShowInformationToUser


class LetTheLearnBegin:
    """
    The following class is used to wrap up the NeuralNetworkModelsController functionality in a readable form.
    It will be useful to give that functionality over to EnumUserOptions and subsequently into the main app controller.
    Tasks:
        1. Read and wrap into the variable directory's path into the training and validation data sets.
        2. Configure a training and validation generator in order to perform data augmentations.
        3. Load data in from directories subsequently create the data batches for the training and validation data sets.
        4. Compile and fit the neural network model. History learning will be saved in the dynamic variable.
        5. Plot in the figure the accuracy and the cost function after the completed learning process.
    """

    @staticmethod
    def starter():
        starter = ConfigureAndRunLearningProcess()

        # Read directories contains training and validation items
        path_to_training_data, path_to_validation_data = starter.readDirectoriesForLearning()

        # Configure a generator for the training and validation data set - get an ImageDataGenerator object
        training_generator_augmentation, validation_generator_augmentation = starter.configureDataAugmentations()

        # Load a training and validation data in from directories into the training generator, turning it into the batches
        training_data_generator, validation_data_generator = starter.createDataBatchesForLearning(
            path_to_training_data, training_generator_augmentation, path_to_validation_data,
            validation_generator_augmentation)

        # Fit the neural network model subsequently start the learning process
        history_learning = starter.compileAndFitNeuralNetworkModel(training_data_generator, validation_data_generator)

        # Plot the accuracy and the cost function for the training history learning as well as validation history learning
        starter.plotAccuracyAndLossValues(history_learning)
        ShowInformationToUser("The training process has been completed. Thank You.").runNotification()
