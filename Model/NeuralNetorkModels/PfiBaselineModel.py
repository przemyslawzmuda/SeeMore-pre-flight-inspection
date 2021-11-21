from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense


class BaselineModel:
    """
    A class used to create a hierarchical structure of the neural network model. The following model is a baseline
    for the future more advanced neural network models.

    Class Object Attributes
    -----------------------------
    recognizeWingComponents : `bool`
        A boolean value of the variable in order to indicate the region of application of the class.
    recognizeAircraftPoundings : `bool`
        A boolean value of the variable in order to indicate the region of application of the class.

    Dynamic Attributes
    -----------------------------
    hidden_activation_function : `object`
        String (name of function) or an instance of the function. Can be used from tfl.keras.activations.
    output_neurons : `int`
        Number of the output neurons in the output layer of the neural network model.
    output_activation_function : `object`
        String (name of function) or an instance of the function. Can be used from tfl.keras.activations.

    Methods
    -----------------------------
    pfi_model_0(self) -> object
        Baseline model for the future more advanced neural network models.
    """

    # Class Object Attributes - actual attributes on that specific class, use anywhere in that class
    recognizeWingComponents = True
    recognizeAircraftPoundings = False

    '''
    Use OOP because the code is well organized, repeatable and memory efficient.
    '''

    if recognizeWingComponents or recognizeAircraftPoundings:
        def __init__(self, hidden_activation_function: object, output_neurons: int, output_activation_function: object):
            """
            Instantiate the baseline model for a neural network.
            :param hidden_activation_function: activation function for the all hidden layers
            :param output_neurons: number of the neurons in the output layer
            :param output_activation_function: activation function for the output layer
            """
            # Attributes (dynamic data) - specific to each class object
            self.hidden_activation_function = hidden_activation_function
            self.output_neurons = output_neurons
            self.output_activation_function = output_activation_function

        def pfi_model_0(self) -> object:
            """
            Baseline model. The ultimate goal of creating a baseline model is attempting at beating the basic model
            to create more sophisticated following models which could be adjusted to the particular problem.
            :return: <keras.engine.sequential.Sequential object at ...(memory location model)...>
            :rtype: object
            """
            pfi_model_0 = Sequential([
                Flatten(),
                Dense(1024, activation=self.hidden_activation_function),
                Dense(512, activation=self.hidden_activation_function),
                Dense(256, activation=self.hidden_activation_function),
                Dense(self.output_neurons, self.output_activation_function)
            ])
            return pfi_model_0
