from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT,  glFlush

class DisplayMaster:
    """
        A class for displaying figure.
        ...
        Attributes
        ----------
        x_center_coordinate, y_center_coordinate: int, int
            coordinates of figure center (used for moving). Both are equal zero by default.

        scaling_coef: float
            equal 1 by defult, increase/decrease by 50% each time changed
        
        figure_color: list
            figure color stored as rgb unsigned byte

        move_vector: list
            two coordinates (-1 or 1) that defines figure moving direction

        list_of_figures_to_draw: list
            stores class-object of geometric figures to draw
    """

    x_center_coordinate = 0
    y_center_coordinate = 0

    scaling_coef = 1

    figure_color = []
    move_vector = []

    def __init__(self, list_of_figures_to_draw, figure_color, move_vector):
        self.list_of_figures_to_draw = list_of_figures_to_draw
        DisplayMaster.figure_color = figure_color
        DisplayMaster.move_vector = move_vector

    def render_figure(self):
        glClear(GL_COLOR_BUFFER_BIT)

        for figure in self.list_of_figures_to_draw:
            figure.draw_me()

        glFlush()