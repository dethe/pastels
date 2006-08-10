import objc
from Foundation import *
from AppKit import NSColor, NSRectFill, NSCompositeSourceAtop
from ScreenSaver import ScreenSaverView
from PastelsPreferencesWindow import *
from brush import Brush
import image_ext


class PastelsView(ScreenSaverView):

    
    def initWithFrame_isPreview_(self, frame, isPreview):
        self = super(PastelsView, self).initWithFrame_isPreview_(frame, isPreview)
        self.registerDefaults()
        width, height, segments, self.showBrush = pastelsPreferences()
        self.brush = Brush(width, height, segments, frame)
        self.image = NSImage.alloc().initWithSize_(self.frame().size)
        self.image.lockFocus()
        NSColor.blackColor().set()
        NSRectFill(self.bounds())
        self.image.unlockFocus()
        self.debugging = False
        return self
    
    def drawInfo(self):
        from geometry import cartToPolarDegrees
        self._debugString(50, 'Vector: (%s, %s)' % self.brush.vector)
        dX,dY = self.brush.vector
        speed,angle = map(int, cartToPolarDegrees(dX,dY))
        self._debugString(30, 'Speed: %s' % speed)
        self._debugString(10, 'Angle: %s' % angle)

    def _debugString(self, y, string):
        a_str = NSAttributedString.alloc().initWithString_attributes_(
            string,
            {NSForegroundColorAttributeName: NSColor.whiteColor()})
        NSColor.blackColor().set()
        rect = (10,y), a_str.size()
        NSRectFill(rect)
        self.setNeedsDisplayInRect_(rect)
        a_str.drawAtPoint_((10,y))
    
    def registerDefaults(self):
        defaults = ScreenSaverDefaults.defaultsForModuleWithName_(appkey)
        defaults.registerDefaults_({u'brushWidth': 32, u'brushHeight': 32,
            u'brushSegments': 16, u'showBrush': True})
        defaults.synchronize()
    
    def animateOneFrame(self):
        self.image.lockFocus()
        self.brush.trail()
        self.setNeedsDisplayInRect_(self.brush.bounds())
        self.brush.move()
        self.brush.rotate()
        self.brush.bounce(self.bounds()[1])
        if self.showBrush:
            self.brush.draw()
            self.setNeedsDisplayInRect_(self.brush.bounds())
        if self.debugging:
            self.drawInfo()
        self.image.unlockFocus()
    
    def keyDown_(self, event):
        import os
        if event.charactersIgnoringModifiers()== 'p':
            print 'Trying to save file'
            NSSound.soundNamed_('Tink').play()
            savepath = os.path.join(NSHomeDirectory(), 'Desktop', 'PastelsSnapshot.png')
            if os.path.exists(savepath):
                version = 0
                path, ext = os.path.splitext(savepath)
                while os.path.exists(savepath):
                    version += 1
                    savepath = '%s%s%s' % (path, version, ext)
            self.image.writeToFilePath_(savepath)
        else:
            print 'trying to process normally'
            super(PastelsView, self).keyDown_(event)
    
    def hasConfigureSheet(self):
        return True
    
    def configureSheet(self):
        return PastelsPreferencesWindow.alloc().initWithFrame_((316,158))
    
    def drawRect_(self, rect):
        self.image.drawInRect_fromRect_operation_fraction_(
            rect,
            rect,
            NSCompositeSourceAtop,
            1.0)

