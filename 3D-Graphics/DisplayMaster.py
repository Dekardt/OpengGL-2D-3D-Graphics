from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from OpenGL.GLUT import glutSwapBuffers

from LightSource import LightSource
from SceneObject import *

class DisplayMaster:
    """
        A class for managing program window. It collects data, initializes window, draws figure, manages keyboard actions.
        ...
        Attributes
        ----------
        light_source: LightSource
            class-object LightSource (i.e. the light itself and the visual envelope (ball))

        list_of_objects_to_draw: list
            list of all figures that must be drawed
        ...
        Methods
        ----------
        __init__():
           Set canvas default parameters as matrix mode, grid etc. Create light source and initializes list of all figures that must be drawed
           
        render_global_picture():
            Render list of all figures
    """
    def __init__(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, 800.0 / 800.0, 0.01, 100.0)

        glMatrixMode(GL_MODELVIEW)

        glEnable(GL_DEPTH_TEST)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)

        glClearColor(0.0, 0.0, 0.0, 0.0)

        self.light_source = LightSource()

        self.list_of_objects_to_draw = []

        #self.list_of_objects_to_draw.append(ObjectCube([0, 0, 0], 7))
        self.list_of_objects_to_draw.append(ObjectSurface(lambda x, y: sin(x) + cos(y)))


    def render_global_picture(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        self.light_source.draw_light_source()

        for object in self.list_of_objects_to_draw:
            object.render_me()

        glutSwapBuffers()