from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense


class TestModel:

    # Class Object Attributes - actual attributes on that specific class, use anywhere in that class
    recognizeWingComponents = True
    recognizeAircraftPoundings = False

    if recognizeWingComponents or recognizeAircraftPoundings:
        def __init__(self, hidden_activation_function: object, output_neurons: int, output_activation_function: object):
            # Attributes (dynamic data) - specific to each class object
            self.hidden_activation_function = hidden_activation_function
            self.output_neurons = output_neurons
            self.output_activation_function = output_activation_function

        def pfi_model_0(self) -> object:
            test_model = Sequential([
                Flatten(),
                Dense(8, activation=self.hidden_activation_function),
                Dense(4, activation=self.hidden_activation_function),
                Dense(self.output_neurons, self.output_activation_function)  # output layer
            ])
            return test_model
