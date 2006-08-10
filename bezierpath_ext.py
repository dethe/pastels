'''
    Refactoring complete 2006-05-12
'''

import objc
from AppKit import NSBezierPath

# Category for NSBezierPath to add ability to stroke for python sequence

class NSBezierPath(objc.Category(NSBezierPath)):
    @classmethod
    def strokePathForPoints_(cls, points):
        path = NSBezierPath.alloc().init()
        path.moveToPoint_(points[0])
        for point in points[1:]:
            path.lineToPoint_(point)
        path.stroke()
