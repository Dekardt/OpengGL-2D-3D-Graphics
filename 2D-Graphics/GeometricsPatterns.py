from OpenGL.GL import glBegin, glEnd, glVertex2f, glColor3ub, GL_TRIANGLES, GL_LINE_LOOP, GL_QUADS

from DisplayMaster import DisplayMaster

class GeometricPattern:
    """
    An abstract class for figure type.
    ...
    Attributes
    ----------
    list_of_vertex: list
        stores list of points that presents this figure (3 for triangle, 4 for quad etc.)
    """

    def __init__(self, list_of_vertex):
        self.list_of_vertex = list_of_vertex

    def draw_me(self):
        pass

class Triangles(GeometricPattern):

    def draw_me(self):

        # figure color
        glColor3ub(DisplayMaster.figure_color[0], DisplayMaster.figure_color[1], DisplayMaster.figure_color[2])

        # drawing figure
        glBegin(GL_TRIANGLES)
        for coords in self.list_of_vertex:
            glVertex2f(DisplayMaster.x_center_coordinate + coords[0] * DisplayMaster.scaling_coef, DisplayMaster.y_center_coordinate + coords[1] * DisplayMaster.scaling_coef)
        glEnd()

        # border color
        glColor3ub(0, 0, 0)

        # drawing border
        glBegin(GL_LINE_LOOP)
        for coords in self.list_of_vertex:
            glVertex2f(DisplayMaster.x_center_coordinate + coords[0] * DisplayMaster.scaling_coef, DisplayMaster.y_center_coordinate + coords[1] * DisplayMaster.scaling_coef)
        glEnd()

class Quads(GeometricPattern):

    def draw_me(self):

        # figure color
        glColor3ub(DisplayMaster.figure_color[0], DisplayMaster.figure_color[1], DisplayMaster.figure_color[2])

        # drawing figure
        glBegin(GL_QUADS)
        for coords in self.list_of_vertex:
            glVertex2f(DisplayMaster.x_center_coordinate + coords[0] * DisplayMaster.scaling_coef, DisplayMaster.y_center_coordinate + coords[1] * DisplayMaster.scaling_coef)
        glEnd()

        # border color
        glColor3ub(0, 0, 0)

        # drawing border
        glBegin(GL_LINE_LOOP)
        for coords in self.list_of_vertex:
            glVertex2f(DisplayMaster.x_center_coordinate + coords[0] * DisplayMaster.scaling_coef, DisplayMaster.y_center_coordinate + coords[1] * DisplayMaster.scaling_coef)
        glEnd()