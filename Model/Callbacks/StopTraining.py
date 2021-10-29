from tensorflow.keras.callbacks import Callback


class StopTrainingCallback(Callback):
    def __init__(self, accuracy: float):
        self.accuracy = accuracy

    def on_epoch_end(self, epoch, logs={}):
        """
        This function should only be called during training process.
        :param epoch:
        :param logs: 
        :return:
        """
        if logs.get('accuracy') > self.accuracy:
            print(f"The value of the accuracy {self.accuracy} of the following model has been reached.")
            self.model.stop_training = True
