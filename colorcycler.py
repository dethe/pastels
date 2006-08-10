'''
    Refactoring completed 2006-05-12
'''

from random import randint
from itertools import islice, cycle
from AppKit import NSColor

# Color Cycler, infinite iterator

# define the ranges to work with
_increasing = range(256)
_decreasing = range(255, -1, -1)


def _rgbaIntsToFloats(red, green, blue):
    '''Our ranges are integers, but NSColor expects floats'''
    return red / 255.0, green / 255.0, blue / 255.0, 1.0

def _nscolor(red, green, blue):
    return NSColor.colorWithCalibratedRed_green_blue_alpha_(
        *_rgbaIntsToFloats(red, green, blue))
        
def _color_cycler():
    '''Increase one color, then decrease the next, repeat'''
    red, green, blue = 255, 0, 0
    for green in _increasing:
        yield _nscolor(red, green, blue)
    for red in _decreasing:
        yield _nscolor(red, green, blue)
    for blue in _increasing:
        yield _nscolor(red, green, blue)
    for green in _decreasing:
        yield _nscolor(red, green, blue)
    for red in _increasing:
        yield _nscolor(red, green, blue)
    for blue in _decreasing:
        yield _nscolor(red, green, blue)

def ColorCycler():
    # start on random color (by discarding until it is reached) and cycle forever
    return islice(cycle(_color_cycler()), randint(0, 256*6), None) 

def test():
    cc = ColorCycler()
    for i in range(20):
        print cc.next()
        
if __name__ == '__main__':
    test()
