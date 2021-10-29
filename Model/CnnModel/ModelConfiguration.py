class ModelConfiguration:
    # Class Object Attribute
    recognizeWingComponents = True
    recognizeAircraftPoundings = False

    '''
    Pillar of OOP: INHERITANCE allows new objects to take on the properties of existing objects.
    Do INTROSPECTION using dir() method on the object.
    '''
    if recognizeWingComponents:
        def __init__(self, model: object, optimizer: object, lossFunction: object, historyName: str,
                     trainingGenerator: object, epochsNumber: int, validationGenerator: object):
            # Attributes (dynamic data):
            if self.recognizeAircraftPoundings or self.recognizeAircraftPoundings:
                self._model = model  # this should be a private variable
                self.optimizer = optimizer  # self refers to the particular object
                self.lossFunction = lossFunction
                self.historyName = historyName
                self.trainingGenerator = trainingGenerator
                self.epochsNumber = epochsNumber
                self.validationGenerator = validationGenerator

    def compileModel(self):
        self._model.compile(
            optimizer=self.optimizer,
            loss=self.lossFunction,
            metrics=["accuracy"]
        )

    def createHistoryAndRunModel(self) -> object:
        self.historyName = self._model.fit(
            self.trainingGenerator,
            epochs=self.epochsNumber,
            validation_data=self.validationGenerator
        )
        return self._historyName
