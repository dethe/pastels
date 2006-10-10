'''
  Refactoring completed 2006-05-12
'''

from AppKit import *
from ScreenSaver import ScreenSaverDefaults

appkey = 'org.livingcode.miniprojects.pastels'


def pastelsPreferences():
    # switch to using defaults.dictionaryForKey_(key) ?
    defaults = ScreenSaverDefaults.defaultsForModuleWithName_(appkey)
    width = defaults.integerForKey_(u'brushWidth')
    height = defaults.integerForKey_(u'brushHeight')
    segments = defaults.integerForKey_(u'brushSegments')
    return width, height, segments

def setPastelsPreferences(width, height, segments):
    # switch to using defaults.setObject_forKey_(dict, key)
    defaults = ScreenSaverDefaults.defaultsForModuleWithName_(appkey)
    defaults.setInteger_forKey_(width, u'brushWidth')
    defaults.setInteger_forKey_(height, u'brushHeight')
    defaults.setInteger_forKey_(segments, u'brushSegments')
    defaults.synchronize()

def Label(text, position):
    label = NSTextField.alloc().initWithFrame_((position, (114,17)))
    label.setSelectable_(False)
    label.setBordered_(False)
    label.setStringValue_(text)
    return label

def Slider(max, default, tag, position):
    slider = NSSlider.alloc().initWithFrame_((position, (164,26)))
    slider.setAllowsTickMarkValuesOnly_(True)
    slider.setMaxValue_(max)
    slider.setMinValue_(4)
    slider.setNumberOfTickMarks_(int(max / 4) + 1)
    slider.setIntValue_(default)
    slider.setTag_(tag)
    return slider

def Button(title, window, position):
    button = NSButton.alloc().initWithFrame_((position, (82,32)))
    button.setButtonType_(NSMomentaryLight)
    button.setBezelStyle_(NSRoundedBezelStyle)
    button.setTitle_(title)
    if title == 'OK':
        button.setKeyEquivalent_(u'\r')
        button.setAction_('fireOK:')
    elif title == 'Cancel':
        button.setAction_('fireCancel:')
    button.setTarget_(window)
    return button

def Window(title, width, height, view=None):
    window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
        ((0,0),(width,height)),
        NSTitledWindowMask |
        NSClosableWindowMask | 
        NSMiniaturizableWindowMask |
        NSResizableWindowMask,
        NSBackingStoreBuffered,
        False)
    window.setTitle_(title)
    if view:
        window.setContentView_(view)
    window.orderFront_(window)
    return window


class PastelsPreferencesWindow(NSWindow):
    def initWithFrame_(self, frame):
        self = super(PastelsPreferencesWindow, self).initWithContentRect_styleMask_backing_defer_(
            ((0,0),frame),
            NSBorderlessWindowMask,
            NSBackingStoreBuffered,
            False)
        self.setReleasedWhenClosed_(False)
        width, height, segments = pastelsPreferences()
        c = self.contentView()
        c.addSubview_(Label(u'Brush Width:', (17,114)))
        c.addSubview_(Label(u'Brush Height:', (17,82)))
        c.addSubview_(Label(u'Brush Segments:', (17,50)))
        c.addSubview_(Slider(128, width, 1, (134, 112)))
        c.addSubview_(Slider(128, height, 2, (134, 80)))
        c.addSubview_(Slider(64, segments, 3, (134, 48)))
        c.addSubview_(Button(u'Cancel', self, (138,2)))
        c.addSubview_(Button(u'OK', self, (220,2)))
        return self
        
    def canBecomeKeyWindow(self):
        return True

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

