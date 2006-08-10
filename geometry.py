from math import sin, cos, pi, sqrt, atan, radians, degrees, acos, asin
from random import choice, randint


# GEOMETRY UTILITIES

DEGREE = pi / 180.0 # one degree in radians


# Opposite of zip() builtin, for sequence of pairs
def unzippairs(seq):
    return [x for x,y in seq],[y for x,y in seq]

def bounds(seq):
    '''Find x,y and width,height of tuple sequence'''
    xseq,yseq = unzippairs(seq)
    x = min(xseq)
    y = min(yseq)
    width = max(xseq) - x
    height = max(yseq) - y
    return [(x,y),(width,height)]

def center(seq):
    '''
    Finds center-point of a sequence
    '''
    position, size = bounds(seq)
    x = position[0] + size[0] / 2.0
    y = position[1] + size[1] / 2.0
    return x,y

def translate(p1, p2):
    ''' Move p1 by p2 in either 2D or 3D coordinates'''
    return tuple([sum(pair) for pair in zip(p1, p2)])

def translateSequence(seq, point):
    ''' Move every point in seq by point in 2D or 3D coordinates'''
    return [translate(pt, point) for pt in seq]    

def polarToCartDegrees(radius, theta):
    # theta is in degrees, convert to radians
    theta = radians(theta)
    return radius * cos(theta), radius * sin(theta)

def cartToPolarDegrees(x,y):
  # returns radius, theta (in degrees)
  # special case axes:
  if x == 0 and y == 0: return 0.0, 0.0 # should this be an error
  elif x == 0 and y > 0: return y, pi / 2.0
  elif x == 0 and y < 0: return -y, 3 * pi / 2.0
  elif y == 0 and x > 0: return x, 0.0
  elif y == 0 and x < 0: return -x, pi
  # special case quadrants
  radius = sqrt(x*x + y*y)
  theta = atan(y/x) # this is only valid for first quadrant (x and y positive)
  if x > 0 and y > 0:
    # first quadrant, we're OK
    pass
  elif x < 0 and y > 0: 
    # second quadrant
    theta += pi 
  elif x < 0 and y < 0: 
    # third quadrant
    theta += pi 
  elif x > 0 and y < 0: 
    # fourth quadrant
    theta += (2.0 * pi) # fourth quadrant
  return radius, degrees(theta)

def rotate(point, angle):
    ''' Rotate a point by angle around pivot point'''
    x,y = point
    x1 = cos(angle) * x - sin(angle) * y
    y1 = sin(angle) * x + cos(angle) * y
    return x1,y1

def rotateSequence(seq, angle):
    return [rotate(point, angle) for point in seq]

def rotateSequenceOnOrigin(seq, angle):
    dX, dY = center(seq)
    seq = translateSequence(seq, (-dX, -dY))
    seq = rotateSequence(seq, angle)
    return translateSequence(seq, (dX, dY))

def rnd():
    '''
    Add a small amount of randomness
    '''
    return choice([-1,0,1])

def rnd3():
    return choice([-3,-2,-2,-1,-1,-1,0,0,0,0,1,1,1,2,2,3])


            
  
