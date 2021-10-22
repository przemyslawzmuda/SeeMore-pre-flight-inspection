class ModelConfiguration:
    # Class Object Attribute - actual attributes on that specific class, use anywhere in that class
    recognizeWingComponents = True
    recognizeAircraftPoundings = True

    def __init__(self, model, optimizer, lossFunction, historyName, trainingGenerator, epochsNumber, validationGenerator):
        # use OOP because the code is well organized, repeatable and memory efficient
        # Attributes (dynamic data) - specific to each class object:
        if self.recognizeAircraftPoundings or self.recognizeAircraftPoundings:
            self.model = model
            self.optimizer = optimizer  # self refers to the particular object
            self.lossFunction = lossFunction
            self.historyName = historyName
            self.trainingGenerator = trainingGenerator
            self.epochsNumber = epochsNumber
            self.validationGenerator = validationGenerator

    def compileModel(self):
        self.model.compile(
            optimizer=self.optimizer,
            loss=self.lossFunction,
            metrics=["accuracy"]
        )

    def createHistoryAndRunModel(self):
        self.historyName = self.model.fit(
            self.trainingGenerator,
            epochs=self.epochsNumber,
            validation_data=self.validationGenerator
        )
        return self.historyName
