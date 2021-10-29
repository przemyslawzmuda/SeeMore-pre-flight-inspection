class ModelConfiguration:
    # Class Object Attribute
    recognizeWingComponents = True
    recognizeAircraftPoundings = False

    if recognizeWingComponents:
        def __init__(self, model: object, optimizer: object, lossFunction: object, historyName: str,
                     trainingGenerator: object, epochsNumber: int, validationGenerator: object):
            # Attributes (dynamic data):
            if self.recognizeAircraftPoundings or self.recognizeAircraftPoundings:
                self.optimizer = optimizer  # self refers to the particular object
                self.lossFunction = lossFunction
                self.historyName = historyName
                self.trainingGenerator = trainingGenerator
                self.epochsNumber = epochsNumber
                self.validationGenerator = validationGenerator

    def compileModel(self, model):
        model.compile(
            optimizer=self.optimizer,
            loss=self.lossFunction,
            metrics=["accuracy"]
        )

    def createHistoryAndRunModel(self, model) -> object:
        self.historyName = model.fit(
            self.trainingGenerator,
            epochs=self.epochsNumber,
            validation_data=self.validationGenerator
        )
        return self.historyName
