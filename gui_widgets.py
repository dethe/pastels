'''
    Refactoring completed 2006-05-12
'''

from AppKit import *

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

def Checkbox(title, default, tag, position):
    checkbox = NSButton.alloc().initWithFrame_((position, (94,18)))
    checkbox.setButtonType_(NSSwitchButton)
    checkbox.setTitle_(title)
    checkbox.setState_(default)
    checkbox.setTag_(tag)
    return checkbox

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


