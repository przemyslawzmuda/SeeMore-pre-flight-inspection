from TestModel import TestModel
from Model.Generator.BasicDataGenerator import BasicZoomGenerator
from Model.Generator.FeedGenerator import FeedDataGenerator
from IO.IOTkinter.DataInputWithTkinter.ChoosePath import InputDirectoryPathWithTkinter
from tensorflow.keras.activations import relu, softmax
from tensorflow.keras.optimizers import Adam
from ModelConfiguration import ModelConfiguration
from Model.SeeMoreSoftware.DrawConlusionsFromDeepLearning.DrawConclusions import DrawConclusionsController


class ConfigureAndRunLearningProcess:
    drawConclusions = DrawConclusionsController()

    # Configure a generator for the training data set - get an ImageDataGenerator object
    training_data_augmentation = BasicZoomGenerator(1./255, [0.1, 0.3]).create_zoom_generator()

    # Configure a generator for the validation data set - get an ImageDataGenerator object
    validation_data_augmentation = BasicZoomGenerator(1./255, [0.1, 0.3]).create_zoom_generator()

    # Load a training data in from directories into the training generator, turning it into the batches
    path_to_training_data = InputDirectoryPathWithTkinter(
        "Choose a directory contains training data").runNotification()
    training_data_generator = FeedDataGenerator(
        path_to_training_data, 100, 10, "categorical").injectDataIntoGenerator(training_data_augmentation)

    # Load a validation data in from directories into the validation generator, turning it into the batches
    path_to_validation_data = InputDirectoryPathWithTkinter(
        "Choose a directory contains validation data").runNotification()
    validation_data_generator = FeedDataGenerator(
        path_to_validation_data, 100, 10, "categorical").injectDataIntoGenerator(validation_data_augmentation)

    # Return a hierarchical structure of the neural network
    artificial_neural_network_model = TestModel(relu, 3, softmax).pfi_model_0()

    # Compile the neural network model
    model_configuration_object = ModelConfiguration(
        Adam, "categorical_crossentropy", training_data_generator, 3, validation_data_generator)
    model_configuration_object.compileModel(artificial_neural_network_model)

    # Fit the neural network model subsequently start the learning process
    history_test = model_configuration_object.createHistoryAndRunModel(artificial_neural_network_model)

    # Plot the accuracy and the cost function for training history learning as well as validation history learning
    drawConclusions.plotLossAccuracyGraph(history_test)
