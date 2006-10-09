from colorcycler import color_generator
from Foundation import NSInsetRect, NSObject
from AppKit import NSRectFill

NUMRECTS = 24

class TunnelBrush(NSObject):
    '''
    A simple screensaver to paint 24 concentric rectangles, running through an endless palette of colours
    '''
    
    def initWithFrame_(self, frame):
        self = super(TunnelBrush, self).init()
        (x,y),(width,height) = frame
        dx = (width - x) / float(NUMRECTS * 2)
        dy = (height - y) / float(NUMRECTS * 2)
        self._rects = [NSInsetRect(frame, i * dx, i * dy) for i in range(NUMRECTS)]
        self._colors = list(color_generator())[::4] # change this number to make the color transitions smoother or faster
        return self
    
    def action(self):
        for idx, rect  in enumerate(self._rects):
            self._colors[idx].set()
            NSRectFill(rect)
        self._colors.append(self._colors.pop(0))
