'''
  Refactoring completed 2006-05-12
'''

from AppKit import NSWindow, NSBorderlessWindowMask, NSBackingStoreBuffered
from AppKit import NSOKButton, NSCancelButton
from ScreenSaver import ScreenSaverDefaults
from gui_widgets import *

appkey = 'org.livingcode.miniprojects.pastels'


def pastelsPreferences():
    defaults = ScreenSaverDefaults.defaultsForModuleWithName_(appkey)
    width = defaults.integerForKey_(u'brushWidth')
    height = defaults.integerForKey_(u'brushHeight')
    segments = defaults.integerForKey_(u'brushSegments')
    showBrush = defaults.boolForKey_(u'showBrush')
    return width, height, segments, showBrush

def setPastelsPreferences(width, height, segments, showBrush):
    defaults = ScreenSaverDefaults.defaultsForModuleWithName_(appkey)
    defaults.setInteger_forKey_(width, u'brushWidth')
    defaults.setInteger_forKey_(height, u'brushHeight')
    defaults.setInteger_forKey_(segments, u'brushSegments')
    defaults.setBool_forKey_(showBrush, u'showBrush')
    defaults.synchronize()


class PastelsPreferencesWindow(NSWindow):
    def initWithFrame_(self, frame):
        self = super(PastelsPreferencesWindow, self).initWithContentRect_styleMask_backing_defer_(
            ((0,0),frame),
            NSBorderlessWindowMask,
            NSBackingStoreBuffered,
            False)
        self.setReleasedWhenClosed_(False)
        width, height, segments, showBrush = pastelsPreferences()
        c = self.contentView()
        c.addSubview_(Label(u'Brush Width:', (17,114)))
        c.addSubview_(Label(u'Brush Height:', (17,82)))
        c.addSubview_(Label(u'Brush Segments:', (17,50)))
        c.addSubview_(Slider(128, width, 1, (134, 112)))
        c.addSubview_(Slider(128, height, 2, (134, 80)))
        c.addSubview_(Slider(64, segments, 3, (134, 48)))
        c.addSubview_(Checkbox(u'Show Brush', showBrush, 4,(18,26)))
        c.addSubview_(Button(u'Cancel', self, (138,2)))
        c.addSubview_(Button(u'OK', self, (220,2)))
        return self

    def fireOK_(self, button):
        c = self.contentView()
        width = c.viewWithTag_(1).intValue()
        height = c.viewWithTag_(2).intValue()
        segments = c.viewWithTag_(3).intValue()
        showBrush = c.viewWithTag_(4).state()
        setPastelsPreferences(width, height, segments, showBrush)
        NSApp().endSheet_returnCode_(self, NSOKButton)

    def fireCancel_(self, button):
        NSApp().endSheet_returnCode_(self, NSCancelButton)

