from random import randint, choice
from math import sqrt, sin, cos, radians
from colorcycler import random_color_cycler
from AppKit import NSBezierPath, NSAffineTransform
from Foundation import NSMidX, NSMidY

# Some utilities for randomizing

def rnd():
    '''
    Add a small amount of randomness
    '''
    return choice([-1,0,1])

def rnd3():
    '''
    Add a small amount of randomness with a curved likelihood
    '''
    return choice([-3,-2,-2,-1,-1,-1,0,0,0,0,1,1,1,2,2,3])
    
def rndPoint(x, y, width, height):
    rx = randint(x, x + width)
    ry = randint(y, y + height)
    return rx, ry
    
# Some utilities for vectors

def vectorFromMagnitude_degrees_(mag, deg):
    angle = radians(deg)
    x = mag * cos(angle)
    y = mag * sin(angle)
    return x,y
    
def vectorMagnitude_(vec):
    x,y = vec
    return sqrt(x**2 + y**2)
    
def vector_rotateByDegrees_(vec, deg):
    matrix = NSAffineTransform.transform()
    matrix.rotateByDegrees_(deg)
    return matrix.transformPoint_(vec)
    
def vector_setMagnitude_(vec, mag):
    matrix = NSAffineTransform.transform()
    matrix.scaleBy_(1.0 / vectorMagnitude_(vec)) # make unit length
    matrix.scaleBy_(mag)
    return matrix.transformPoint_(vec)


class Brush(NSBezierPath):

    def initWithSize_noSegments_inFrame_(self, size, noSegments, frame):
        self = super(NSBezierPath, self).init()
        self.windowSize = windowWidth, windowHeight = frame[1]
        self.position = (windowWidth / 2, windowHeight / 2)
        self.size = width, height = size
        
        # Draw some random lines within a box of size
        box_x = -(width / 2)
        box_y = -(height / 2)
        self.moveToPoint_(rndPoint(box_x, box_y, width, height))
        for x in range(noSegments):
            self.lineToPoint_(rndPoint(box_x, box_y, width, height))
        # move from origin 
        self.position = dX, dY = rndPoint(0, 0, windowWidth, windowHeight) # start in random location
        self.translateXBy_yBy_(dX, dY)
        
        self.color = random_color_cycler()
        self.speed = randint(1,7) # initial speed of movement
        initial_angle = randint(0, 359) # initial direction of movement
        self.rotation = randint(0,23) # initial degrees of rotation
        self.vector = vectorFromMagnitude_degrees_(self.speed, initial_angle)
        return self
        
    def origin(self):
        box = self.bounds()
        return NSMidX(box), NSMidY(box)
        
    def action(self):
        self.rotate()
        self.move()
        self.bounce()
        self.draw()
        
    def move(self):
        dx,dy = self.vector
        matrix = NSAffineTransform.transform()
        matrix.translateXBy_yBy_(dx,dy)
        self.position = matrix.transformPoint_(self.position)
        self.transformUsingAffineTransform_(matrix)
        
    def translateXBy_yBy_(self, x, y):
        matrix = NSAffineTransform.transform()
        matrix.translateXBy_yBy_(x,y)
        self.transformUsingAffineTransform_(matrix)

    def rotateByDegrees_(self, rotation):
        matrix = NSAffineTransform.transform()
        matrix.rotateByDegrees_(rotation)
        self.transformUsingAffineTransform_(matrix)
    
    def rotate(self):
        x, y = self.position
        # note: offset x and y by some amount for spiraling or circling effects
        x += 50
        y += 50
        self.translateXBy_yBy_(-x,-y)
        self.rotateByDegrees_(self.rotation)
        self.translateXBy_yBy_(x,y)

    def bounce(self):
        '''
        In addition to bouncing the brush, reverse the spin of the brush and
        introduce small bits of randomness into angle, speed, and spin.
        '''
        x,y = self.position
        dx,dy = self.vector
        width,height = self.size
        width,height = width/2.0, height/2.0
        dX, dY = self.vector
        windowWidth, windowHeight = self.windowSize
        if (x < -width and dX < 0) or (x > (width + windowWidth) and dX > 0): 
            self.add_randomness()
            self.vector = -dx, dy
        if (y < -height and dY < 0) or (y > (height + windowHeight) and dY > 0):
            self.vector = self.vector[0], -self.vector[1] # can't just use dX, -dY in case where we flip both
        if vectorMagnitude_(self.vector) < 1.0:
            self.vector = vector_setMagnitude_(self.vector, 1.0)

    def add_randomness(self):
        self.speed = self.speed + rnd() or 1
        self.rotation = (self.rotation + rnd()) * -1
        self.vector = vector_rotateByDegrees_(self.vector, rnd3())
        self.vector = vector_setMagnitude_(self.vector, self.speed)

    def draw(self):
        self.color.next().set()
        self.stroke()


