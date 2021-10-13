from tensorflow.keras.preprocessing.image import ImageDataGenerator


class BasicGenerator:
    def __init__(self, **kwargs):
        self.rotation_range = kwargs.get("rotation_range")
        self.width_shift_range = kwargs.get("width_shift_range")
        self.height_shift_range = kwargs.get("height_shift_range")
        self.brightness_range = kwargs.get("brightness_range")
        self.shear_range = kwargs.get("shear_range")
        self.zoom_range = kwargs.get("zoom_range")
        self.fill_mode = kwargs.get("fill_mode")
        self.horizontal_flip = kwargs.get("horizontal_flip")
        self.vertical_flip = kwargs.get("vertical_flip")
        self.rescale = kwargs.get("rescale")

    @staticmethod
    def createGenerator(**kwargs):
        return ImageDataGenerator(**kwargs)
