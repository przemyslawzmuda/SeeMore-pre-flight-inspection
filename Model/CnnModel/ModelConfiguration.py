class ModelConfiguration:
    # Class Object Attribute
    recognizeWingComponents = True
    recognizeAircraftPoundings = False

    if recognizeWingComponents:
        def __init__(self, model: object, optimizer: object, lossFunction: object, historyName: str,
                     trainingGenerator: object, epochsNumber: int, validationGenerator: object, **kwargs):
            # Attributes (dynamic data):
            if self.recognizeAircraftPoundings or self.recognizeAircraftPoundings:
                self.optimizer = optimizer  # self refers to the particular object
                self.lossFunction = lossFunction
                self.historyName = historyName
                self.trainingGenerator = trainingGenerator
                self.epochsNumber = epochsNumber
                self.validationGenerator = validationGenerator
                # Use keyword arguments to for the __init__() method to overload a constructor
                self.callback = kwargs.get('ownCallback')

    def compileModel(self, model):
        model.compile(
            optimizer=self.optimizer,
            loss=self.lossFunction,
            metrics=["accuracy"]
        )

    def createHistoryAndRunModel(self, model) -> object:
        if self.callback:
            self.historyName = model.fit(
                self.trainingGenerator,
                epochs=self.epochsNumber,
                validation_data=self.validationGenerator,
                callbacks=self.callback
            )
            return self.historyName
        else:
            self.historyName = model.fit(
                self.trainingGenerator,
                epochs=self.epochsNumber,
                validation_data=self.validationGenerator,
            )
            return self.historyName
