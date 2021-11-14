import matplotlib.pyplot as mpyplot


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
