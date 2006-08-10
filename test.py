from gui_widgets import Window
from PastelsView import PastelsView
from PyObjCTools import AppHelper
from AppKit import NSObject, NSApplication, NSTimer, NSApp

width, height = 640, 480

class MyAppDelegate(NSObject):

    def applicationDidFinishLaunching_(self, notification):
        rect = ((0,0),(width, height))
        self.pastels_view = PastelsView.alloc().initWithFrame_isPreview_(rect, False)
        self.pastels_view.debugging = True
        self.window = Window('Pastels Test', width, height, self.pastels_view)
        self.window_delegate = MyWindowDelegate.alloc().init()
        self.window.setDelegate_(self.window_delegate)
        self.timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            0.001,
            self.pastels_view,
            'animateOneFrame',
            None,
            True)
        
class MyWindowDelegate(NSObject):

    def windowWillClose_(self, notification):
        NSApp().terminate_(self)


if __name__ == "__main__":
    app_delegate = MyAppDelegate.alloc().init()
    NSApplication.sharedApplication().setDelegate_(app_delegate)   
    AppHelper.runEventLoop(installInterrupt=True)


