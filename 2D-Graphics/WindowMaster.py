from OpenGL.GLUT import *
from OpenGL.GL import glClearColor, glViewport, glMatrixMode, glLoadIdentity, GL_PROJECTION, GL_MODELVIEW
from OpenGL.GLU import gluOrtho2D

from Initializer import Initializer
from DisplayMaster import DisplayMaster


class WindowMaster:
    """
        A class for managing program window. It collects data, initializes window, draws figure, manages keyboard actions.
        ...
        Attributes
        ----------
        background_color: list
            background color stored as rgb unsigned byte

        data_initializer: Initializer
            object of class Initializer used to read and store input data
        
        displayer: DisplayMaster
            object of class DisplayMaster used to draw main figure
        ...
        Methods
        ----------
        create_window():
            Create window, set background color and grid size

        start_drawing():
            Start main loop.

        reshape_window(width, heigth):
            Manage changing window's size

        keyboardControl():
            Managing keyboard actions
    """
    def create_window(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(800, 800)
        glutInitWindowPosition(320, 100)
        glutCreateWindow("lab1")
        glClearColor(self.background_color[0], self.background_color[1], self.background_color[2], 1.0)
        gluOrtho2D(-20.0, 20.0, -20.0, 20.0)

    def __init__(self):
        self.data_initializer = Initializer('sw_templates.json')
        self.background_color = [color/255 for color in self.data_initializer.get_background_color()]
        self.create_window()
        self.displayer = DisplayMaster(self.data_initializer.get_all_figure_list(), self.data_initializer.get_figure_color(), self.data_initializer.get_move_vector())

    def startDrawing(self):
        glutDisplayFunc(self.displayer.renderFigure)
        glutReshapeFunc(self.reshapeWindow)
        glutKeyboardFunc(self.keyboardControl)
        glutMainLoop()

    def reshapeWindow(self, w, h):
        if h == 0:
            h = 1

        koef = float(w) / h
        glViewport(0, 0, w, h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        if w > h:
            gluOrtho2D(-20.0 * koef, 20.0 * koef, -20.0, 20.0)
        else:
            gluOrtho2D(-20.0, 20.0, -20.0 / koef, 20.0 / koef)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def keyboardControl(self, key, x1, y1):

        key = ord(key)

        if key == 100 or key == 119:
            DisplayMaster.x_center_coordinate = DisplayMaster.x_center_coordinate + DisplayMaster.move_vector[0]
            DisplayMaster.y_center_coordinate = DisplayMaster.y_center_coordinate + DisplayMaster.move_vector[1]
        if key == 97 or key == 115:
            DisplayMaster.x_center_coordinate = DisplayMaster.x_center_coordinate - DisplayMaster.move_vector[0]
            DisplayMaster.y_center_coordinate = DisplayMaster.y_center_coordinate - DisplayMaster.move_vector[1]
        if key == 43:
            DisplayMaster.scaling_coef = DisplayMaster.scaling_coef * 1.5
        if key == 45:
            DisplayMaster.scaling_coef = DisplayMaster.scaling_coef / 1.5
        glutPostRedisplay()