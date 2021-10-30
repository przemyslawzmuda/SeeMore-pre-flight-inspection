from tensorflow.keras.preprocessing.image import ImageDataGenerator


class BasicGenerator:
    def __init__(self, rescale: float):
        """
        If the rescaling factor is provided, the data will be multiplied by the provided factor.
        The ultimate goal of the rescaling factor is normalizing pixels value into float range: (0, 1).
        :param rescale: rescaling factor, defaults to None.
        """
        self.rescale = rescale

    def createGenerator(self) -> object:
        """
        :rtype: <class 'keras.preprocessing.image.ImageDataGenerator'>
        """
        return ImageDataGenerator(rescale=self.rescale)
