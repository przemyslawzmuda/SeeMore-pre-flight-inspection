class ModelConfiguration:
    """A class used to configure a neural network model in oder to start a learning process.

    Class Object Attributes
    ----------
    recognizeWingComponents : bool and recognizeAircraftPoundings : `bool`
        A boolean value of the variable in order to indicate the region of application of the class.
    all_history_names : `list`
        A list which stores history_name variables passed during the initializing of the instance.
    all_ModelConfiguration_instances : `list`
        A list which stores all instances of the following class (stores objects).

    Dynamic Attributes
    ----------
    optimizer : `object` or `str`
        String (name of optimizer) or an instance of the optimizer. Can be used from tfl.keras.optimizers.
    lossFunction : `object` or `str`
        String (name of a loss function) or an instance of the loss function. Can be used from tlf.keras.losses.
    history_name : `str`
        Variable name in order to indicate and retrieve the training metrics on completion the learning process.
    trainingGenerator : `object`
        An instance of the ImageDataGenerator class for the training data.
    validationGenerator : `object`
        An instance of the ImageDataGenerator class for the validation data.
    epochsNumber : `int`
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
    recognizeWingComponents = True
    recognizeAircraftPoundings = False

    # Use Class Object Attribute to track all history_name variables used during compiling the model
    all_history_names = []

    # Use Class Object Attribute to track all the given instances of the class
    all_ModelConfiguration_instances = []

    # Using Class Object Attributes define for what type of problems the ModelConfiguration is valid to implement
    if recognizeWingComponents or recognizeAircraftPoundings:
        def __init__(self, optimizer: object or str, lossFunction: object or str, history_name: str,
                     trainingGenerator: object, epochsNumber: int, validationGenerator: object, **kwargs):
            """
            The following constructor enables to initialize the crucial parameters needed during compiling
            the neural network model.

            :param optimizer: String (name of optimizer) or an instance of the optimizer --> tfl.keras.optimizers.
            :param lossFunction: String (name of a loss function) or an instance of the loss function.
            :param history_name: String (name of the training history saved during the learning).
            :param trainingGenerator: An instance of the ImageDataGenerator class for the training data.
            :param epochsNumber: A number of the estimated epochs during the training process.
            :param validationGenerator:  An instance of the ImageDataGenerator class for the validation data.
            :param kwargs: onwCallback=[...] --> pass the list of the metrics (ex.: customized callback).
            """

            # Attributes (dynamic data):
            self.optimizer = optimizer  # self refers to the particular object
            self.lossFunction = lossFunction

            self.history_name = history_name
            ModelConfiguration.all_history_names.append(self.history_name)

            self.trainingGenerator = trainingGenerator
            self.epochsNumber = epochsNumber
            self.validationGenerator = validationGenerator
            # Use keyword arguments in the __init__() method in order to overload the constructor
            self.callback = kwargs.get('ownCallback')

            # Append an instance object into the Class Object Attribute
            ModelConfiguration.all_ModelConfiguration_instances.append(self)

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
            loss=self.lossFunction,
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
            self.history_name = model.fit(
                self.trainingGenerator,
                epochs=self.epochsNumber,
                validation_data=self.validationGenerator,
                callbacks=self.callback
            )
            return self.history_name
        else:
            self.history_name = model.fit(
                self.trainingGenerator,
                epochs=self.epochsNumber,
                validation_data=self.validationGenerator,
            )
            return self.history_name
