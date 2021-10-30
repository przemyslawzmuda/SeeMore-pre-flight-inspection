from tensorflow.keras.preprocessing.image import ImageDataGenerator
from BasicDataGenerator import BasicGenerator


class DataAugmentation(BasicGenerator):
    """
    DataGenerator is used to generate batches of tensor image WITH real-time data augmentation.
    """

    def __init__(self, rescale: float, rotation_range: int, brightness_range: list, horizontal_flip: bool,
                 vertical_flip: bool, width_shift_range: float, height_shift_range: float):
        super(BasicGenerator, self).__init__(rescale)
        self.rotation_range = rotation_range
        self.brightness_range = brightness_range
        self.horizontal_flip = horizontal_flip
        self.vertical_flip = vertical_flip
        self.width_shift_range = width_shift_range
        self.height_shift_range = height_shift_range

    def createGenerator(self) -> object:
        """
        :rtype: <class 'keras.preprocessing.image.ImageDataGenerator'>
        """
        return ImageDataGenerator(rescale=self.rescale,
                                  rotation_range=self.rotation_range,
                                  width_shift_range=self.width_shift_range,
                                  height_shift_range=self.height_shift_range,
                                  brightness_range=self.brightness_range,
                                  horizontal_flip=self.horizontal_flip,
                                  vertical_flip=self.vertical_flip)

