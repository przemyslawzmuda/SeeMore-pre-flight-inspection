import tensorflow as tfl
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from tensorflow.keras.activations import softmax, relu


class PfiModel:
    def __init__(self, optimizer, lossFunction, historyName, trainingGenerator, epochsNumber, validationGenerator):
        self.optimizer = optimizer
        self.lossFunction = lossFunction
        self.historyName = historyName
        self.trainingGenerator = trainingGenerator
        self.epochsNumber = epochsNumber
        self.validationGenerator = validationGenerator

    @staticmethod
    def pfi_wing_0_1_0():
        tfl.keras.Sequential([
            Conv2D(10, kernel_size=(2, 2), activation=relu, input_shape=(300, 300, 3)),
            MaxPool2D(pool_size=(2, 2)),
            Conv2D(10, kernel_size=(2, 2), activation=relu),
            MaxPool2D(pool_size=(2, 2)),
            Flatten(),
            Dense(1024, activation=relu),
            Dense(512, activation=relu),
            Dense(256, activation=relu),
            Dense(20, activation=softmax)
        ])

    def compileModel(self, model):
        model.compile(
            optimizer=self.optimizer,
            loss=self.lossFunction,
            metrics=["accuracy"]
        )

    def createHistoryAndRunModel(self, historyName, model, trainingGenerator, epochsNumber, validationGenerator):
        historyName = model.fit(
            trainingGenerator,
            epochs=epochsNumber,
            validation_data=validationGenerator
        )
