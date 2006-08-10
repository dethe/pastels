from random import randint
from colorcycler import ColorCycler
from geometry import *
from bezierpath_ext import NSBezierPath

class Brush(object):

    '''
    Simple python class to manage state for a random squiggle drawing
    expressed as an list of points
    '''

    def __init__(self, width, height, segments, frame):
        max_x = width - 1
        max_y = height - 1
        count = range(segments + 1)
        self.path =[(randint(0, max_x), randint(0, max_y)) for i in count]
        self.color = ColorCycler()
        self.rotation = DEGREE * 3
        self.vector = polarToCartDegrees(randint(1,7), randint(0,359))
        # move path to random start position
        dX = randint(width, frame[1][0] - width)
        dY = randint(height, frame[1][1] - height)
        self.path = translateSequence(self.path, (dX,dY))
        self._setBounds()

    def _setBounds(self):
        self._bounds = bounds(self.path)
        self.position = self._bounds[0]
        self.size = self._bounds[1]

    def bounds(self):
        return self._bounds

    def rotate(self):
        self.path = rotateSequenceOnOrigin(self.path, self.rotation)
        self._setBounds()

    def move(self):
        self.path = translateSequence(self.path, self.vector)
        self._setBounds()

    def bounce(self, size):
        '''
        In addition to bouncing the brush, reverse the spin of the brush and
        introduce small bits of randomness into angle, speed, and spin.
        '''
        x,y = self.position
        width,height = self.size
        width,height = width/2.0, height/2.0
        dX, dY = self.vector
        speed,angle = map(int, cartToPolarDegrees(dX, dY))
        windowWidth, windowHeight = size
        if (x < -width and dX < 0) or (x + width > windowWidth and dX > 0): 
            speed = speed + rnd() or 1
            angle += rnd3()
            x,y = polarToCartDegrees(speed, angle)
            self.vector = -x, y
            self.rotation = self.rotation * -1 + rnd() * DEGREE
        if (y < -height and dY < 0) or (y + height > windowHeight and dY > 0):
            speed = speed + rnd() or 1
            angle += rnd3()
            x,y = polarToCartDegrees(speed, angle)
            self.vector = x,-y
            self.rotation = self.rotation * -1 + rnd() * DEGREE
        while self.vector == (0,0):
            self.vector = rnd(),rnd()

    def trail(self):
        self.color.next().set()
        NSBezierPath.strokePathForPoints_(self.path)

    def draw(self):
        NSColor.blackColor().set()
        NSBezierPath.strokePathForPoints_(self.path)

