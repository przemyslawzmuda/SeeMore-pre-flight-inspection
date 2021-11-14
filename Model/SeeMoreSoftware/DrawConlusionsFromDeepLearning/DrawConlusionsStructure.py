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
