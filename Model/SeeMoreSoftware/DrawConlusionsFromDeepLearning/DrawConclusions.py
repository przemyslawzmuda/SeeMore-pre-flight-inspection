import matplotlib.pyplot as mpyplot
from DrawConlusionsStructure import ConclusionsStructure
from IO.IOTkinter.DataInputWithTkinter.ChoosePath import InputFilePathWithTkinter
from IO.IOTkinter.DataInputWithTkinter.DataInput import AskUserForIntegerNumber, AskUserForString


class DrawConclusionsController:
    def __init__(self):
        self.preprocessConlusions = ConclusionsStructure()

    def plotLossAccuracyGraph(self, model_history):

        # Set the y-axis values
        accuracy_values = model_history.history["accuracy"]
        validation_accuracy_values = model_history.history["val_accuracy"]
        loss_values = model_history.history["loss"]
        validation_loss_values = model_history.history["val_loss"]

        # Set the x-axis values
        x_axis_values = range(len(model_history.history["loss"]))  # epochs number

        mpyplot.figure(figsize=(20, 10))

        # Visualize the accuracy values
        mpyplot.subplot(1, 2, 1)
        mpyplot.plot(x_axis_values, accuracy_values, label="accuracy")
        mpyplot.plot(x_axis_values, validation_accuracy_values, label="val_accuracy")
        mpyplot.title("Accuracy")
        mpyplot.xlabel("Epochs number")
        mpyplot.legend()

        # Visualize the validation accuracy
        mpyplot.subplot(1, 2, 2)
        mpyplot.plot(x_axis_values, loss_values, label="loss")
        mpyplot.plot(x_axis_values, validation_loss_values, label="val_loss")
        mpyplot.title("Loss")
        mpyplot.xlabel("Epochs number")
        mpyplot.legend()

        mpyplot.show()

    def plotPredictionsForChosenCustomImage(self):

        path_to_custom_image = InputFilePathWithTkinter(
            "Choose a path for custom image in order to make a prediction and subsequently plot a graph with "
            "the prediction.").runNotification()

        target_custom_image_shape = AskUserForIntegerNumber(
            "Enter the target shape of the custom image").runNotification()

        data_from_configured_generator = AskUserForString(
            "Enter the name of the configured ImageDataGenerator object in order to "
            "retrieve a class's names").runNotification()

        neural_network_model = InputFilePathWithTkinter(
            "Choose a path to the saved neural network model").runNotification()

        data_to_plot_tuple = \
            self.preprocessConlusions.makePredictionForOneImage(path_to_custom_image, target_custom_image_shape,
                                                                data_from_configured_generator, neural_network_model)

        image_to_plot, title_image, image_predictions = data_to_plot_tuple

        mpyplot.figure(figsize=(8, 6))
        mpyplot.subplot(1, 1, 1)
        self.preprocessConlusions.plotPredictedImage(image_to_plot, title_image)
        mpyplot.subplot(1, 1, 1)
        self.preprocessConlusions.plotPredictedValues(image_to_plot, title_image, image_predictions)
        mpyplot.show()
