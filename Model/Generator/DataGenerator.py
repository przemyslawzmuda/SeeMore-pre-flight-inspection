from tensorflow.keras.preprocessing.image import ImageDataGenerator
from BasicDataGenerator import BasicZoomGenerator


"""
MRO - Method Resolution Order
Use name_method.mro() - check the order (MRO) of that class. The hierarchical way of inheritance. 
MRO goes through all parent classes and inherited classes and creates the inheritance model (hierarchy of inheritances).
"""


class DataAugmentation(BasicZoomGenerator):
    """
    DataAugmentation is used to generate batches of tensor image WITH real-time data augmentation.
    """

    def __init__(self, rescale: float, zoom_range: list, rotation_range: int, brightness_range: list, horizontal_flip: bool,
                 vertical_flip: bool, width_shift_range: float, height_shift_range: float):
        super().__init__(rescale, zoom_range)
        self.rotation_range = rotation_range
        self.brightness_range = brightness_range
        self.horizontal_flip = horizontal_flip
        self.vertical_flip = vertical_flip
        self.width_shift_range = width_shift_range
        self.height_shift_range = height_shift_range

    def create_generator(self) -> object:
        """
        The following function performs data augmentation applying given parameters.
        :rtype: <class 'keras.preprocessing.image.ImageDataGenerator'>
        """
        return ImageDataGenerator(rescale=self.rescale,
                                  zoom_range=self.zoom_range,
                                  rotation_range=self.rotation_range,
                                  width_shift_range=self.width_shift_range,
                                  height_shift_range=self.height_shift_range,
                                  brightness_range=self.brightness_range,
                                  horizontal_flip=self.horizontal_flip,
                                  vertical_flip=self.vertical_flip)
