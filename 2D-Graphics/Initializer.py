import json
from GeometricsPatterns import *

class Initializer:
    """
        A class for reading and storing data from json file.
        ...
        Attributes
        ----------
        file_name : str
            name of the source file
        file_data : dict
            key - data type name, value - data stored as list(moving vector, color etc.)
            or as list of list (figure's points)
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.read_data()

    def read_data(self):
        with open(self.file_name) as jsonFile:
            file_content = jsonFile.read()
            self.file_data = json.loads(file_content)

    def get_background_color(self):
        return self.file_data['backgroundColor']

    def get_figure_color(self):
        return self.file_data['figureColor']

    def get_move_vector(self):
        return self.file_data['vector']

    def get_all_figure_list(self):
        figures_to_draw = []
        all_figure_list = self.file_data['figure']

        for list_of_vertex in all_figure_list['triangle']:
            figures_to_draw.append(Triangles(list_of_vertex))

        for list_of_vertex in all_figure_list['quad']:
            figures_to_draw.append(Quads(list_of_vertex))

        return figures_to_draw