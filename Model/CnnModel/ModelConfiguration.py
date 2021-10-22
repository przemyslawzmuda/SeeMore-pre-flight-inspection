class ModelConfiguration:
    # Class Object Attribute - actual attributes on that specific class, use anywhere in that class
    recognizeWingComponents = True
    recognizeAircraftPoundings = True

    def __init__(self, model: object, optimizer: object, lossFunction: object, historyName: str,
                 trainingGenerator: object, epochsNumber: int, validationGenerator: object):
        # use OOP because the code is well organized, repeatable and memory efficient
        # Attributes (dynamic data) - specific to each class object:
        if self.recognizeAircraftPoundings or self.recognizeAircraftPoundings:
            self._model = model  # this should be a private variable
            self._optimizer = optimizer  # self refers to the particular object
            self._lossFunction = lossFunction
            self._historyName = historyName
            self._trainingGenerator = trainingGenerator
            self._epochsNumber = epochsNumber
            self._validationGenerator = validationGenerator

    def compileModel(self):
        self._model.compile(
            optimizer=self._optimizer,
            loss=self._lossFunction,
            metrics=["accuracy"]
        )

    def createHistoryAndRunModel(self) -> object:
        self._historyName = self._model.fit(
            self._trainingGenerator,
            epochs=self._epochsNumber,
            validation_data=self._validationGenerator
        )
        return self._historyName
