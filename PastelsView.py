import objc
from Foundation import *
from AppKit import NSColor, NSRectFill, NSCompositeSourceAtop
from ScreenSaver import ScreenSaverView
from PastelsPreferencesWindow import *
#from brush import Brush
#from brush2 import TunnelBrush
from brush3 import BouncingBrush

class PastelsView(ScreenSaverView):
    
    def initWithFrame_isPreview_(self, frame, isPreview):
        self = super(PastelsView, self).initWithFrame_isPreview_(frame, isPreview)
        self.registerDefaults()
        width, height, segments = pastelsPreferences()
        #self.brush = Brush.alloc().initWithSize_noSegments_inFrame_((width,height), segments, frame)
        #self.brush = TunnelBrush.alloc().initWithFrame_(frame)
        self.brush = BouncingBrush.alloc().initWithFrame_(frame)
        self.setAnimationTimeInterval_(0.001)
        return self
            
    def registerDefaults(self):
        defaults = ScreenSaverDefaults.defaultsForModuleWithName_(appkey)
        defaults.registerDefaults_({u'brushWidth': 32, u'brushHeight': 32,
            u'brushSegments': 16})
        defaults.synchronize()
        
    def animateOneFrame(self):
        self.brush.action()
     
    def keyDown_(self, event):
        if event.charactersIgnoringModifiers()== 'p':
            self.saveToFile()
            NSSound.soundNamed_('Tink').play()
        else:
            super(PastelsView, self).keyDown_(event)

    def nextFilename(self):
        import os
        savepath = os.path.join(NSHomeDirectory(), 'Desktop', 'PastelsSnapshot.png')
        if os.path.exists(savepath):
            version = 0
            path, ext = os.path.splitext(savepath)
            while os.path.exists(savepath):
                version += 1
                savepath = '%s%s%s' % (path, version, ext)
        return savepath
    
    def saveToFile(self):
        self.lockFocus()
        image_rep = NSBitmapImageRep.alloc().initWithFocusedViewRect_(self.bounds())
        self.unlockFocus()
        data = image_rep.representationUsingType_properties_(NSPNGFileType, None)
        data.writeToFile_atomically_(self.nextFilename(), False)
    
    def hasConfigureSheet(self):
        return True
    
    def configureSheet(self):
        return PastelsPreferencesWindow.alloc().initWithFrame_((316,158))
    
    def drawRect_(self, rect):
        self.lockFocus()
        NSColor.blackColor().set()
        NSRectFill(self.bounds())
        self.unlockFocus()        
 
