from tensorflow.keras.preprocessing.image import ImageDataGenerator


class BasicGenerator:
    """
    BasicGenerator is used to generate batches of tensor image WITHOUT real-time data augmentation.
    """

    def __init__(self, rescale: float):
        """
        If the rescaling factor is provided, the data will be multiplied by the provided factor.
        The ultimate goal of the rescaling factor is normalizing pixels value into float range: (0, 1).
        :param rescale: rescaling factor, defaults to None.
        """
        self.rescale = rescale

    def create_basic_generator(self) -> object:
        """
        The following function performs normalizing pixels data into the range between 0 and 1: (0, 1).
        :rtype: <class 'keras.preprocessing.image.ImageDataGenerator'>
        """
        return ImageDataGenerator(rescale=self.rescale)


class BasicZoomGenerator(BasicGenerator):
    """
    BasicZoomGenerator is used to generate batches of tensor image WITH real-time data augmentation applying
    zoom parameter.
    """

    def __init__(self, rescale: float, zoom_range: list):
        """
        :param rescale: rescaling factor, defaults to None.
        :param zoom_range: Float or list [lower, upper]. Range for random zoom.
        """
        super(BasicGenerator, self).__init__(rescale)
        self.zoom_range = zoom_range

    def create_zoom_generator(self) -> object:
        """
        The following function performs normalizing pixels data into the range between 0 and 1 applying rescaling
        factor, as well as this performs data augmentation applying zooming factor.
        :rtype: <class 'keras.preprocessing.image.ImageDataGenerator'>
        """
        return ImageDataGenerator(rescale=self.rescale, zoom_range=self.zoom_range)
