import keras.callbacks


class DisplayLogs(keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs=None):
        print(
            "The average loss for epoch {} is {:7.2f} ".format(
                epoch, logs["loss"]
            )
        )

