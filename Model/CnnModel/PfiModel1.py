from PfiBaselineModel import BaselineModel
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense


class PfiModel1(BaselineModel):
    # Overrides Class Object Attributes
    recognizeWingComponents = True
    recognizeAircraftPoundings = True

    if recognizeWingComponents or recognizeAircraftPoundings:
        def __init__(self, hidden_activation_function: object, output_activation_function: object, output_neurons: int,
                     conv_activation_function: object, number_filters: int, rows: int, columns: int, channels: int, **kwargs):

            # super() refers to the class above, not necessary to pass the self keyword
            super().__init__(hidden_activation_function, output_neurons, output_activation_function)
            self.conv_activation_function = conv_activation_function
            self.number_filters = number_filters
            self.rows = rows
            self.columns = columns
            self.channels = channels
            self.kernel_size = kwargs.get('kernel_size')
            self.pool_size = kwargs.get('pool_size')

    def pfi_model_1(self) -> object:

        pfi_model_1 = Sequential([
            Conv2D(self.number_filters, self.kernel_size, activation=self.conv_activation_function, input_shape=(self.rows, self.columns, self.channels)),
            MaxPool2D(self.pool_size),
            Conv2D(self.number_filters, self.kernel_size, activation=self.conv_activation_function),
            MaxPool2D(self.pool_size),
            Flatten(),
            Dense(1024, self.hidden_activation_function),
            Dense(512, self.hidden_activation_function),
            Dense(256, self.hidden_activation_function),
            Dense(self.output_neurons, self.output_activation_function)
        ])

        return pfi_model_1
