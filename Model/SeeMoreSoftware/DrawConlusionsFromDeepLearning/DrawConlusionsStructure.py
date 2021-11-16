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

    def normalizeImage(self, path_to_image: str, image_shape: int) -> object:
        """
        The following function enables to upload a custom image and prepare it in order to make a prediction
        using convolutional neural network. The function transforms a custom image into a tensor matrix and reshapes it
        into the following format: (image_shape, image_shape, colour_channels).
        Attention:
        The parameter image_shape shall be compatible with the parameter input_shape prescribed in a convolutional
        neural network.
        :param path_to_image: Absolute path into the custom image.
        :param image_shape: The desired shape of the normalized image.
        :return: <class 'tensorflow.python.framework.ops.EagerTensor'>
        """

        try:
            '''
            This operation returns a tensor with the entire contents of the input filename. It does not do any parsing, 
            it just returns the contents as they are. Usually, this is the first step in the input pipeline. 
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
            expand_animations=True -> An optional bool. Defaults to True. Controls the shape of the returned 
            op's output. If True, the returned op will produce a 3-D tensor for PNG, JPEG, and BMP files; 
            and a 4-D tensor for all GIFs, whether animated or not. If, False, the returned op will produce a 3-D tensor 
            for all file types and will truncate animated GIFs to the first frame.
            '''
            decoded_image = tfl.io.decode_image(image, channels=3, expand_animations=True)  # True is default value
            print(decoded_image)
            '''
            decoded_image:

            tf.Tensor(
            [[[168 161 117]
              [168 161 117]
              [168 161 117]
              ...
              [223 210 176]
              [223 210 176]
              [223 210 176]]], shape=(4032, 3024, 3), dtype=uint8)
            '''

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

            # <class 'tensorflow.python.framework.ops.EagerTensor'>
            return normalized_image

            '''
            The following function returns a Tensor() data type image:

            tf.Tensor(
                [[[0.65882355 0.6313726  0.45882353]
                  [0.6509804  0.62352943 0.4509804]
                 [0.64705884 0.61960787 0.45490196]
                    ...
            [0.8745098
            0.8235294
            0.6862745]
            [0.8745098  0.8235294  0.6862745]
            [0.8666667
            0.8156863
            0.6784314]]], shape = (400, 400, 3), dtype = float32)
            '''

        except ValueError as err:
            DisplayErrorNotification(f"Unable to normalize an image because of {err}.").runNotification()

    def makePredictionForOneImage(self, path_to_image: str, image_shape: int, data_generator: object,
                                  model: object) -> tuple:
        """
        The following function reads a custom image, performs a process of normalizing that image as well as this,
        makes a prediction for that image.
        :param path_to_image: Absolute path into the image,
        :param image_shape: size=[image_shape, image_shape] -> A 1-D int32 Tensor of 2 elements: new_height, new_width.
                The new size for the images.
        :param data_generator: A configured data generator used during the training.
        :param model: Configured Neural Network model used during the training.
        :return: output_tuple = (extended_normalized_image, image_prediction_class)
        """

        # Upload a custom image and preprocess it
        normalized_image = self.normalizeImage(path_to_image, image_shape)
        # normalized_image object: tf.Tensor([...], shape = (image_shape, image_shape, 3), dtype = float32)

        # Extend the dimensions of the normalized image into a 4D format -> 'batch image' = (batch_size, size, size, 3)
        extended_normalized_image = tfl.expand_dims(normalized_image, axis=0)

        # Make a prediction
        image_predictions = model.predict(extended_normalized_image)

        # Get class names from generator
        class_names_from_generator = self.getClassNamesFromGenerator(data_generator)

        # Add logic for multi-class in order to choose the correct class's name
        if len(image_predictions[0]) > 1:
            image_prediction_class = class_names_from_generator[tfl.argmax(image_predictions[0])]
        else:
            image_prediction_class = class_names_from_generator[int(tfl.round(image_predictions[0]))]

        # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
        output_tuple = tuple((extended_normalized_image, image_prediction_class, image_predictions))
        return output_tuple

    def plotPredictedImage(self, data_to_plot: tuple):
        """
        The following function display a custom image with the estimated name.
        :param data_to_plot: Data in tuple obtained from makePredictionForOneImage() function.
        """
        image_to_plot, title_image, image_predictions = data_to_plot

        mpyplot.imshow(image_to_plot)
        mpyplot.title(f"Prediction: {title_image}")
        mpyplot.axis(False)

    def plotPredictedValues(self, image_to_predict: object, title_image_to_predict: str,
                            image_predictions_values_list: list):

        # Assign class numbers into the variable in order to plot the probability for each class
        class_numbers_to_predictions = len(image_predictions_values_list[0])

        # Get or set the current tick locations and labels of the x-axis.
        mpyplot.xticks(range(class_numbers_to_predictions))

        '''
        Plot yticks - Make a bar plot
        The bars are positioned at x with the given alignment. Their dimensions are given by height and width.
        The vertical baseline is bottom (default 0).
        
        matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
        x: float or array-like -> The x coordinates of the bars. See also align for 
            the alignment of the bars to the coordinates. -> range(class_numbers_to_predictions)
        height: float or array-like -> The height(s) of the bars. -> image_predictions_values_list
        '''
        mpyplot.bar(range(class_numbers_to_predictions), image_predictions_values_list, color="#262179")

        # Get or set the y-limits of the current axes.
        mpyplot.ylim([0, 1])

        mpyplot.title(f"Prediction: {title_image_to_predict}")
        mpyplot.ylabel("Probability [%]")
        mpyplot.xlabel("Classes names")
        mpyplot.grid(axis="y")
