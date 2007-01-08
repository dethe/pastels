from Foundation import *
from AppKit import *
import applesms
from third.vector import vector

class BouncingBrush(NSObject):
    '''
    A screensaver which demonstrates Apple's Sudden Motion Sensor (SMS), based on an Io demo program
    '''
    
    def initWithFrame_(self, frame):
        self = super(BouncingBrush, self).init()
        (x,y),(width,height) = frame
        self.position = vector(25,0, 0)
        self.velocity = vector(2, 2, 0)
        self.acceleration = vector(0, 0, 0)
        self.radius = 32
        self.brush_size = [self.radius * 2] * 2
        self.elasticity = .66
        self.friction = .995
        self.setBounds((width, height))
        self.initBrush()
        return self
        
    def initBrush(self):
        self.brush = NSImage.alloc().initWithSize_(self.brush_size)
        self.brush.lockFocus()
        circle = NSBezierPath.alloc().init()
        circle.appendBezierPathWithOvalInRect_(((0,0), self.brush_size))
        NSColor.whiteColor().set()
        circle.fill()
        self.brush.unlockFocus()
    
    def setBounds(self, bounds):
        self.bounds = bounds
        self.minPosition = vector(0,0,0)
        self.maxPosition = vector(bounds[0] - self.radius, bounds[1] - self.radius, 0)

    def move(self):
        self.acceleration = vector(applesms.coords())
        self.acceleration *= -.002

        self.velocity += self.acceleration
        self.velocity *= self.friction
        self.position += self.velocity
        self.position[2] = 0

        if self.position[0] < self.minPosition[0]:
            self.position[0] = self.minPosition[0]
            self.velocity[0] *=  -self.elasticity
        elif self.position[0] > self.maxPosition[0]:
            self.position[0] = self.maxPosition[0]
            self.velocity[0] *= -self.elasticity
        if self.position[1] < self.minPosition[1]:
            self.position[1] = self.minPosition[1]
            self.velocity[1] *= -self.elasticity
        elif self.position[1] > self.maxPosition[1]:
            self.position[1] = self.maxPosition[1]
            self.velocity[1] *= -self.elasticity
            
    def draw(self):
        self.brush.dissolveToPoint_fraction_(self.position[:2], 0.05);  
            
    def action(self):
        self.move()
        self.draw()

