class ModelConfiguration:
    """A class used to configure a neural network model in oder to start a learning process.

    Class Object Attributes
    ----------
    recognize_wing_components : bool and recognize_aircraft_poundings : `bool`
        A boolean value of the variable in order to indicate the region of application of the class.
    all_history_names : `list`
        A list which stores history_name variables passed during the initializing of the instance.
    all_model_configuration_instances : `list`
        A list which stores all instances of the following class (stores objects).

    Dynamic Attributes
    ----------
    optimizer : `object` or `str`
        String (name of optimizer) or an instance of the optimizer. Can be used from tfl.keras.optimizers.
    loss_function : `object` or `str`
        String (name of a loss function) or an instance of the loss function. Can be used from tlf.keras.losses.
    history_name : `str`
        Variable name in order to indicate and retrieve the training metrics on completion the learning process.
    training_generator : `object`
        An instance of the ImageDataGenerator class for the training data.
    validation_generator : `object`
        An instance of the ImageDataGenerator class for the validation data.
    epochs_number : `int`
        A number of the estimated epochs during the training process.
    **kwargs
        ownCallback : `list`
        A list which contains string values of the customized callbacks.

    Methods
    ----------
    compileModel(model: object) -> None
        The following function can be used to compile a hierarchical neural network model in order to
        start the learning process.
    createHistoryAndRunModel(model: object) -> object
        The following method is used to start the learning process.
    """

    # Class Object Attributes - Define default values
    recognize_wing_components = True
    recognize_aircraft_poundings = False

    # Use Class Object Attribute to track all history_name variables used during compiling the model
    all_history_names = []

    # Use Class Object Attribute to track all the given instances of the class
    all_model_configuration_instances = []

    # Using Class Object Attributes define for what type of problems the ModelConfiguration is valid to implement
    if recognize_wing_components or recognize_aircraft_poundings:
        def __init__(self, optimizer: object or str, loss_function: object or str, training_generator: object,
                     epochs_number: int, validation_generator: object, **kwargs):
            """
            The following constructor enables to initialize the crucial parameters needed during compiling
            the neural network model.

            :param optimizer: String (name of optimizer) or an instance of the optimizer --> tfl.keras.optimizers.
            :param loss_function: String (name of a loss function) or an instance of the loss function.
            :param history_name: String (name of the training history saved during the learning).
            :param training_generator: An instance of the ImageDataGenerator class for the training data.
            :param epochs_number: A number of the estimated epochs during the training process.
            :param validation_generator:  An instance of the ImageDataGenerator class for the validation data.
            :param kwargs: onwCallback=[...] --> pass the list of the metrics (ex.: customized callback).
            """

            # Attributes (dynamic data):
            self.optimizer = optimizer  # self refers to the particular object
            self.loss_function = loss_function
            self.training_generator = training_generator
            self.epochs_number = epochs_number
            self.validation_generator = validation_generator
            # Use keyword arguments in the __init__() method in order to overload the constructor
            self.callback = kwargs.get('ownCallback')

            # Append an instance object into the Class Object Attribute
            ModelConfiguration.all_model_configuration_instances.append(self)

    def compileModel(self, model: object) -> None:
        # Use a reStructuredText Example for documentation
        """
        The following function can be used to compile a hierarchical neural network model in order to
        start the learning process.

        :param model: A hierarchical structure of the neural network.
        :type model: object

        :returns: None
        :rtype: None
        """

        model.compile(
            optimizer=self.optimizer(),
            loss=self.loss_function,
            metrics=["accuracy"]
        )

    def createHistoryAndRunModel(self, model: object) -> object:
        # Use a NumPy/SciPy Docstrings Example for documentation
        """The following method is used to start the learning process.

        Parameters
        ----------------------------
        model : object
            A compiled hierarchical structure of the neural network.

        Returns
        ----------------------------
        history_name : object
            A history object. Its History.history attribute is a record of training loss values and metrics values
            at successive epochs, as well as validation loss values and validation metrics values (if applicable).

        Raises
        ----------------------------
        RunTimeError
            The following exception would be raised:
            --> if the model was never compiled;
            --> if the model.fit was wrapped in tfl.function.

        ValueError
            The following exception would be raised, if the mismatched between the provided input data and what
            the model excepts occurred or when the input data was empty.
        """

        if self.callback:
            return model.fit(
                self.training_generator,
                epochs=self.epochs_number,
                validation_data=self.validation_generator,
                callbacks=[self.callback]
            )
        else:
            return model.fit(
                self.training_generator,
                epochs=self.epochs_number,
                validation_data=self.validation_generator,
            )
