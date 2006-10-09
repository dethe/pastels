'''
    Refactoring completed 2006-05-12
    Another refactoring on 2006-08-31
'''

from random import randint
from itertools import cycle
from AppKit import NSColor

# Color Cycler, infinite iterator

COLOR_BLOCK = 256
DOUBLE_BLOCK = COLOR_BLOCK * 2

# define the color ranges to work with
increasing = [x / float(COLOR_BLOCK - 1) for x in range(COLOR_BLOCK)]
decreasing = increasing[::-1]

red = [0.0] * DOUBLE_BLOCK + increasing + [1.0] * DOUBLE_BLOCK + decreasing
green = red[DOUBLE_BLOCK:] + red[:DOUBLE_BLOCK]
blue = green[DOUBLE_BLOCK:] + green[:DOUBLE_BLOCK]

def nscolor(red, green, blue):
    return NSColor.colorWithCalibratedRed_green_blue_alpha_(red, green, blue, 1.0)
        
def color_generator(rgb=None):
    '''Increase one color, then decrease the next, repeat
       Generates 6 * 256 saturated colors'''
    if not rgb:
        rgb = zip(red, green, blue)
    for r,g,b in rgb:
        yield nscolor(r,g,b)
        
def random_color_generator():
    rgb = zip(red, green, blue)
    split = randint(0, len(rgb))
    rand_rgb = rgb[split:] + rgb[:split]
    return color_generator(rand_rgb)    

def color_cycler():
    # generator which cycles forever
    return cycle(color_generator())
    
def random_color_cycler():
    return cycle(random_color_generator())

def test():
    cc = list(color_generator())
    print 'length: %d (expected: %d)' % (len(cc), (256 * 6))
    def d(fl): # float (0.0 -> 1.) to integer (0 - 255)
        return int(fl * 255)
    def c(co):
        return '0x%02X%02X%02X' % (d(co.redComponent()), d(co.greenComponent()), d(co.blueComponent()))
    for i in range(COLOR_BLOCK):
        ix = [i + COLOR_BLOCK * m for m in range(6)]
        print '\t'.join([c(cc[ii]) for ii in ix])
        
if __name__ == '__main__':
    test()
