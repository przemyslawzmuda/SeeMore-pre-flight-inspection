class TrainingGenerator:
    def __init__(self, dataGenerator, pathToTrainingData, targetSize, batchSize, classMode, shuffle):
        self.dataGenerator = dataGenerator
        self.pathToTrainingData = pathToTrainingData
        self.targetSize = targetSize
        self.batchSize = batchSize
        self.classMode = classMode
        self.shuffle = shuffle

    def configureGenerator(self):
        return self.dataGenerator.flow_from_directory(
            self.pathToTrainingData,
            target_size=self.targetSize,
            batch_size=self.batchSize,
            class_mode=self.classMode,
            shuffle=self.shuffle
        )
