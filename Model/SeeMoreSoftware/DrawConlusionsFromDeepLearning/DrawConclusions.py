import matplotlib.pyplot as mpyplot


class DrawConclusionsController:

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

    def getClassNamesFromGenerator(self, data_from_generator: object) -> list:
        """
        The following function returns the list contains class names from a configured TensorFlow generator.
        The dictionary containing the mapping from class names to class indices can be obtained
        via the attribute class_indices. It works for 'flow_from_directory' method in ImageDataGenerator object.
        Classes can be accessed through the classes Args of 'flow_from_directory'. Optional list of class subdirectories
        (e.g. ['dogs', 'cats']). Default: None. If not provided, the list of classes will be automatically inferred from
        the subdirectory names/structure under directory, where each subdirectory will be treated as a different class
        (and the order of the classes, which will map to the label indices, will be alphanumeric).

        :param data_from_generator: Configured object generator, ex.: ImageDataGenerator
        :return: class_names_list
        """
        # Use List comprehension
        class_names_list = [key for key in data_from_generator.class_indices.keys()]
        return class_names_list
