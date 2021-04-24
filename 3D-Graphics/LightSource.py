from OpenGL.GL import glColor3f, glTranslate, glLightfv, glLoadIdentity, GL_LIGHT0, GL_POSITION, GL_DIFFUSE, GL_CONSTANT_ATTENUATION, GL_QUADRATIC_ATTENUATION
from OpenGL.GLU import gluNewQuadric, gluQuadricOrientation, gluSphere, GLU_INSIDE
from OpenGL.GLUT import glutPostRedisplay

from math import sin, cos, pi

class LightSource:
    """
        A class for creating light source
        ...
        Attributes
        ----------
        theta_light_angle: int
            Angle between light vector and Oy in spherical coordinates, 45 degrees by default, increase/decrease by 1 degrees each second

        phi_light_angle: int
            Angle between light vector and Oz in spherical coordinates, 45 degrees by default, increase/decrease by 1 degrees each second

        light_color: list
            light color stored as rbg unsigned byte

        vertical_rotation: bool
            define plane of rotation, true if vertical, false by default - horizontal. May be changed by clicking "t"
        ...
        Methods
        ----------
        __init__(light_color_vector=[1.0, 1.0, 1.0]):
           Set light source default parameters and draw visual envelope

        draw_light_source():
            draw visual envelope

        idle_light_animation_func():
            Function executed in main loop need for light source moving animation
    """
    def __init__(self, light_color_vector=[1.0, 1.0, 1.0]):

        self.theta_light_angle = 45
        self.phi_light_angle = 45

        self.light_color = light_color_vector

        self.vertical_rotation = False

        self.draw_light_source()

    def draw_light_source(self):

        glColor3f(1.0, 1.0, 1.0)

        # 15 is radius of the sphere that light source around
        self.light_source_position = [
            15 * sin(self.theta_light_angle * pi / 180) * sin(self.phi_light_angle * pi / 180),
            15 * cos(self.theta_light_angle * pi / 180),
            15 * sin(self.theta_light_angle * pi / 180) * cos(self.phi_light_angle * pi / 180)
        ]

        glTranslate(self.light_source_position[0], self.light_source_position[1], self.light_source_position[2])
        # set light source position
        glLightfv(GL_LIGHT0, GL_POSITION, [*self.light_source_position, 1])
        # set light color
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.light_color)
        # set light intensity
        glLightfv(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.7)
        glLightfv(GL_LIGHT0,  GL_QUADRATIC_ATTENUATION, 0.0001)

        # turning the rays of light so that the back of the ball is shaded
        gl_q = gluNewQuadric()
        gluQuadricOrientation(gl_q, GLU_INSIDE)

        # draw visual envelope (ball)
        gluSphere(gl_q, 1, 20, 20)

        glLoadIdentity()

    def idle_light_animation_func(self):

        if self.vertical_rotation:
            self.theta_light_angle += 1
        else:
            self.phi_light_angle += 1

        self.draw_light_source()

        glLoadIdentity()
        glutPostRedisplay()