import os

from IO.IOTkinter.DataInputWithTkinter.ChoosePath import InputDirectoryPathWithTkinter
from Model.SeeMoreSoftware.SeeMorePreprocesing.SeeMorePreprocessing import SeeMorePreprocessingSoftware


class SaveTensorFlowModel:
    """
    Call saveModel to save a model's architecture, weights, and training configuration in a single file/folder.
    This allows you to export a model so it can be used without access to the original Python code*.
    Since the optimizer-state is recovered, you can resume training from exactly where you left off.

    An entire model can be saved in two different file formats (SavedModel and HDF5). The TensorFlow SavedModel format
    is the default file format in TF2.x. However, models can be saved in HDF5 format.

    Saving a fully-functional model is very useful—you can load them in TensorFlow.js (Saved Model, HDF5) and then train
    and run them in web browsers, or convert them to run on mobile devices using TensorFlow Lite (Saved Model, HDF5).

    *Custom objects (e.g. subclassed models or layers) require special attention when saving and loading.
    See the Saving custom objects section below
    """

    chooseDirectory = InputDirectoryPathWithTkinter("Choose a directory where the TensorFlow model "
                                                    "will be saved.")
    preprocessSoftware = SeeMorePreprocessingSoftware()

    def __init__(self, model_name):
        self.model_name = model_name

    def saveModel(self):
        """
        The SavedModel format is another way to serialize models. Models saved in this format can be restored using
        tf.keras.models.load_model and are compatible with TensorFlow Serving.
        """

        directory_path = self.chooseDirectory.return_directory_path()
        path_to_save_model = os.path.join(directory_path, "Saved-TensorFlow-Models")
        self.preprocessSoftware.createNewFolder(path_to_save_model)
        filePath = os.path.join(path_to_save_model, self.model_name)
        self.model_name.save(filePath)
