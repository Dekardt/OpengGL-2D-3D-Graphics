from OpenGL.GL import glColor3f, glBegin, glEnd, glNormal3f, glVertex3f,  glLoadIdentity, glTranslate, GL_LINES
from OpenGL.GLUT import glutSolidCube

from abc import ABCMeta, abstractmethod

from math import sin, cos

class SceneObject:
    """
        A an abstract class of objects that must be drawed
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def render_me(self):
        return


class ObjectSurface(SceneObject):
    """
        A class for creating surface that must be drawed
        ...
        Methods
        ----------
        surface_function(x, y):
            Define function that presents surface
        
        calculate_vertex_normal(vertex):
            Calculate normal vector for passed vertex

        render_me():
            Render surface
    """
    def __init__(self):
        pass

    def surface_function(self, x, y):
        return sin(x) + cos(y)

    def calculate_vertex_normal(self, vertex):

        step = 0.5

        #get neighbor vertexes for passed vector to calculate normal
        addit_point_1 = [vertex[0] + step, self.surface_function(vertex[0] + step, vertex[2]), vertex[2]]
        addit_point_2 = [vertex[0], self.surface_function(vertex[0], vertex[2] + step), vertex[2] + step]

        v1 = [c2 - c1 for c1, c2 in zip(vertex, addit_point_2)]
        v2 = [c2 - c1 for c1, c2 in zip(vertex, addit_point_1)]

        #calculate normal
        normal = [v1[1] * v2[2] - v1[2] * v1[1],
                  v1[2] * v2[0] - v1[0] * v2[2],
                  v1[0] * v2[1] - v1[1] * v2[0]]

        return normal

    def render_me(self):

        glColor3f(0.75, 0.3, 0.66)
        #glColor3f(1, 1, 1)

        #surface bounds
        x_lower_bound = -10
        x_upper_bound = 10
        y_lower_bound = -10
        y_upper_bound = 10

        step = 0.5

        x_current = x_lower_bound + step
        y_current = y_lower_bound + step

        #draw part of surface
        glBegin(GL_LINES)

        while x_current <= x_upper_bound + 0.0001:

            while y_current < y_upper_bound + 0.0001:
                normal = self.calculate_vertex_normal([x_current,
                                                       self.surface_function(x_current, y_current),
                                                       y_current])
                glNormal3f(normal[0], normal[1], normal[2])
                glVertex3f(x_current, self.surface_function(x_current, y_current), y_current)

                y_current += step

            y_current = y_lower_bound + step
            x_current += step

        x_current = x_lower_bound + step
        y_current = y_lower_bound + step

        #draw part of surface
        while y_current <= y_upper_bound + 0.01:

            while x_current <= x_upper_bound + 0.01:
                normal = self.calculate_vertex_normal([x_current,
                                                       self.surface_function(x_current, y_current),
                                                       y_current])
                glNormal3f(normal[0], normal[1], normal[2])
                glVertex3f(x_current, self.surface_function(x_current, y_current), y_current)

                x_current += step

            x_current = x_lower_bound + step
            y_current += step

        glEnd()


class ObjectCube(SceneObject):
    """
        A class for creating cube that must be drawed
        ...
        Methods
        ----------
        __init__(position, side_size):
            Init cube position and size
        
        render_me():
            Render cube
    """
    def __init__(self, position, side_size):
        self.position = position
        self.side_size = side_size

    def render_me(self):
        glColor3f(1, 1, 1)

        glLoadIdentity()

        glTranslate(self.position[0], self.position[1], self.position[2])

        glutSolidCube(self.side_size)

        glLoadIdentity()