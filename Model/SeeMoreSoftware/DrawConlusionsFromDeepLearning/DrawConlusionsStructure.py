import tensorflow as tfl
from tensorflow.keras.models import load_model
import matplotlib.pyplot as mpyplot
from IO.IOTkinter.DataOutputWithTkinter.DisplayNotifications import DisplayErrorNotification


class BaselineGraph:
    """
    The following class presents a baseline to configure and display graph using matplotlib library.
    """

    def __init__(self, graph_size: tuple, columns_number: int, rows_number: int):
        """
        Base constructor to initialize the graph.
        :param graph_size: Figure dimension (width, height) in inches.
        :param columns_number: The number of columns in the graph.
        :param rows_number: The number of rows in the graph.
        """

        self.graph_size = graph_size
        self.column_num = columns_number
        self.row_num = rows_number
        self.num_sub_graphs = columns_number * rows_number

    def showSubGraph(self, x_axis_value: list, y_axis_value: list, label_name: str):
        mpyplot.plot(x_axis_value, y_axis_value, label=label_name)

    def configureGraph(self, title_graph: str, index_sub_graph: int, title_x_label: str,
                       x_axis_value: list, y_axis_value: list, label_name: str):

        mpyplot.subplot(self.row_num, self.column_num, index_sub_graph)
        self.showSubGraph(x_axis_value, y_axis_value, label_name)
        mpyplot.title(title_graph)
        mpyplot.xlabel(title_x_label)
        mpyplot.legend()

    def plotGraph(self, title_graph: str, index: int, title_x_label: str, x_axis_value: list,
                  y_axis_value: list, label_name: str):
        """
        The following function will display a configured graph.
        :param title_graph: Title of the graph as a string.
        :param index: The number of position in the graph. Ex.: (1, 2, 1) -> (row: 1, column: 2, position: 1)
        :param title_x_label: The title of the X axis.
        :param x_axis_value: List contains x-values to display.
        :param y_axis_value: List contains y-values to display.
        :param label_name:
        """
        mpyplot.figure(figsize=self.graph_size)
        self.configureGraph(title_graph, index, title_x_label, x_axis_value, y_axis_value, label_name)
        mpyplot.show()


class ConclusionsStructure:

    def getClassNamesFromGenerator(self, data_from_generator: object) -> list:
        """
        The following function returns the list contains class names from a configured TensorFlow generator.
        The dictionary containing the mapping from class names to class indices can be obtained
        via the attribute class_indices. It works for 'flow_from_directory' method in ImageDataGenerator object.
        Classes can be accessed through the classes Args of 'flow_from_directory'. Optional list of class subdirectories
        (e.g. ['dogs', 'cats']). Default: None. If not provided, the list of classes will be automatically inferred from
        the subdirectory names/structure under directory, where each subdirectory will be treated as a different class
        (and the order of the classes, which will map to the label indices, will be alphanumeric).

        :param data_from_generator: Configured object generator, ex.: ImageDataGenerator
        :return: class_names_list
        """
        # Use List comprehension
        class_names_list = [key for key in data_from_generator.class_indices.keys()]
        return class_names_list

    def returnModelSummary(self, model: object):
        return model.summary()

    def loadSavedModel(self, path_to_saved_model: str):
        """
        If the original model was compiled, and saved with the optimizer, then the returned model will be compiled.
        Otherwise, the model will be left uncompiled. In the case that an uncompiled model is returned, a warning
        is displayed if the compile argument is set to True.
        Loads a model saved via model.save()

        :param path_to_saved_model: An absolute path to the saved model. - String or pathlib.Path object,
            path to the saved model or h5py.File object from which to load the model.
        :return: A Keras model instance.
        """

        try:
            loaded_model = load_model(path_to_saved_model, compile=True)
            return loaded_model
        except ImportError:
            DisplayErrorNotification("Unable to load a model from hdf5 or h5py format file.").runNotification()
        except IOError:
            DisplayErrorNotification("Unable to load a model because of an invalid savefile.").runNotification()

    def normalizeImage(self, path_to_image: str, image_shape: int):
        """
        The following function enables to upload a custom image and prepare it in order to make a prediction
        using convolutional neural network. The function transforms a custom image into a tensor matrix and reshapes it
        into the following format: (image_shape, image_shape, colour_channels).
        Attention:
        The parameter image_shape shall be compatible with the parameter input_shape prescribed in a convolutional
        neural network.
        :param path_to_image: Absolute path into the custom image.
        :param image_shape: The desired shape of the normalized image.
        :return: tensor image.
        """

        try:
            '''
            This operation returns a tensor with the entire contents of the input filename. It does not do any parsing, it 
            just returns the contents as they are. Usually, this is the first step in the input pipeline. 
            Reads the contents of file:
            '''
            image = tfl.io.read_file(path_to_image)

            '''
            Function for decode_bmp, decode_gif, decode_jpeg, and decode_png. Detects whether an image is a BMP, GIF, 
            JPEG, or PNG, and performs the appropriate operation to convert the input bytes string into 
            a Tensor of type dtype.
            Returns: Tensor with type dtype and a 3- or 4-dimensional shape, depending on the file type and the value 
            of the expand_animations parameter.
            Args: 
            contents=image -> A Tensor of type string. 0-D. The encoded image bytes.
            channels=3 -> An optional int. Defaults to 0. Number of color channels for the decoded image.
            expand_animations=True -> An optional bool. Defaults to True. Controls the shape of the returned op's output. 
            If True, the returned op will produce a 3-D tensor for PNG, JPEG, and BMP files; and a 4-D tensor for all GIFs, 
            whether animated or not. If, False, the returned op will produce a 3-D tensor for all file types and will 
            truncate animated GIFs to the first frame.
            '''
            decoded_image = tfl.io.decode_image(image, channels=3, expand_animations=True)  # True is default value

            '''
            Resize the image into the prescribed size suing the specified method.
            
            Args:
            images=decoded_image -> 4-D Tensor of shape [batch, height, width, channels] or 
                3-D Tensor of shape [height, width, channels].
            size=[image_shape, image_shape] -> A 1-D int32 Tensor of 2 elements: new_height, new_width. 
                The new size for the images.
                
            Returns:
            If images was 4-D, a 4-D float Tensor of shape [batch, new_height, new_width, channels]. 
            If images was 3-D, a 3-D float Tensor of shape [new_height, new_width, channels].
            '''
            resized_image = tfl.image.resize(decoded_image, size=[image_shape, image_shape])

            # Normalize an image into the float pixels value
            normalized_image = resized_image / 255.0

            return normalized_image

        except ValueError as err:
            DisplayErrorNotification(f"Unable to normalize an image because of {err}.").runNotification()
