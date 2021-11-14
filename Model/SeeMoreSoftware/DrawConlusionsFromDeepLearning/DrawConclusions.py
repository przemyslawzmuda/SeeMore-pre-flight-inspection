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
