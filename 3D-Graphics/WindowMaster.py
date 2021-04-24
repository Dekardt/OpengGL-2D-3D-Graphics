from OpenGL.GL import glViewport, glMatrixMode, glLoadIdentity, glScalef, GL_PROJECTION, GL_MODELVIEW
from OpenGL.GLU import gluPerspective, gluLookAt
from OpenGL.GLUT import *

from math import sin, cos, pi

from DisplayMaster import DisplayMaster

class WindowMaster:
    """
        A class for managing program window. It initializes window, draws figure, manages keyboard actions and camera moving.
        ...
        Attributes
        ----------
        window_width, window_height: int, int
            window's width and height

        theta_angle: int
            Angle between camera vector and Oy in spherical coordinates, 45 degrees by default, increase/decrease by 8 degrees each time changed

        phi_angle: int
            Angle between camera vector and Oz in spherical coordinates, 45 degrees by default, increase/decrease by 8 degrees each time changed
        
        canvas: DisplayMaster
            object of class DisplayMaster used to draw main figure

        scaling_coef: float
            equal 1 by defult, increase/decrease by 10% each time changed
        ...
        Methods
        ----------
        __init__():
            Create window, set attributes by default

        start_drawing():
            Start main loop.

        reshape_function(width, heigth):
            Manage changing window's size and camera moving

        keyboard_control_function():
            Manage keyboard actions

        recalculate_camera_settings():
            Manage changing camera pozition
    """
    def __init__(self):

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutInitWindowSize(800, 800)
        glutInitWindowPosition(320, 100)
        glutCreateWindow("Dzyubchik_CG_L3_V8")

        self.canvas = DisplayMaster()

        self.theta_angle = 45
        self.phi_angle = 45

        self.window_width = 800
        self.window_height = 800

        self.scale_factor = 1

    def start_drawing(self):
        glutDisplayFunc(self.canvas.render_global_picture)
        glutReshapeFunc(self.reshape_function)
        glutKeyboardFunc(self.keyboard_control_function)
        glutIdleFunc(self.canvas.light_source.idle_light_animation_func)
        glutMainLoop()

    def reshape_function(self, w, h):

        # prevent dividing by zero if window height is 0
        if h == 0:
            h = 1

        self.window_width = w
        self.window_height = h

        proportional_rate = float(w) / h

        glViewport(0, 0, w, h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(60.0, proportional_rate, 0.1, 100)

        camera_settings_matrix = [0 for i in range(9)]

        # calculate camera's point of view
        camera_settings_matrix = self.recalculate_camera_settings(camera_settings_matrix)

        # set camera's point of view
        gluLookAt(camera_settings_matrix[0], camera_settings_matrix[1], camera_settings_matrix[2],
                  camera_settings_matrix[3], camera_settings_matrix[4], camera_settings_matrix[5],
                  camera_settings_matrix[6], camera_settings_matrix[7], camera_settings_matrix[8])

        glScalef(self.scale_factor, self.scale_factor, self.scale_factor)

        glMatrixMode(GL_MODELVIEW)

    def keyboard_control_function(self, key, x, y):

        key = key.decode("utf-8").lower()

        if key == 'a':
            self.phi_angle = (self.phi_angle + 8) % 360

        elif key == 'd':
            self.phi_angle = (self.phi_angle - 8) % 360

        elif key == 'w':
            self.theta_angle = (self.theta_angle + 8) % 360

        elif key == 's':
            self.theta_angle = (self.theta_angle - 8 + 360) % 360

        elif key == 'm':
            self.scale_factor *= 1.1

        elif key == 'n':
            self.scale_factor *= 0.9

        elif key == 't':
            self.canvas.light_source.vertical_rotation = not self.canvas.light_source.vertical_rotation

        self.reshape_function(self.window_width, self.window_height)

    def recalculate_camera_settings(self, camera_settings_matrix):

        # 25 is radius of the sphere that camera moves around
        z_camera_coordinate = 25 * sin(self.theta_angle * pi / 180) * cos(self.phi_angle * pi / 180)
        x_camera_coordinate = 25 * sin(self.theta_angle * pi / 180) * sin(self.phi_angle * pi / 180)
        y_camera_coordinate = 25 * cos(self.theta_angle * pi / 180)

        camera_settings_matrix[0] = x_camera_coordinate
        camera_settings_matrix[1] = y_camera_coordinate
        camera_settings_matrix[2] = z_camera_coordinate

        # this if_statements prevents the camera from scrolling when it passes a point perpendicular to the xOz plane
        if self.theta_angle > 180:
            camera_settings_matrix[7] = -1
        else:
            camera_settings_matrix[7] = 1

        return camera_settings_matrix