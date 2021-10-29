from tensorflow.keras.callbacks import Callback


class StopTrainingCallback(Callback):
    def __init__(self, accuracy: float):
        """
        :param accuracy: the value of the training accuracy as a float number. If the given accuracy value is reached,
        the training process will be terminated.
        """
        self.accuracy = accuracy

    def on_epoch_end(self, epoch, logs={}):
        """
        This function should only be called during training process.
        :param epoch: number of the epoch
        :param logs: metric results for the following training epoch
        """
        if logs.get('accuracy') > self.accuracy:
            print(f"The value of the accuracy {self.accuracy} of the following model has been reached.")
            self.model.stop_training = True
