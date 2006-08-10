from objc import Category
from AppKit import *
from os.path import splitext

_fileRepresentationMapping = {
        '.png': NSPNGFileType,
        '.gif': NSGIFFileType,
        '.jpg': NSJPEGFileType,
        '.jpeg': NSJPEGFileType,
        '.bmp': NSBMPFileType,
        '.tif': NSTIFFFileType,
        '.tiff': NSTIFFFileType,
    }

def _getFileRepresentationType(filepath):
    base, ext = splitext(filepath)
    return _fileRepresentationMapping[ext.lower()]

class NSImage(Category(NSImage)):

    def rect(self):
        return (0,0),self.size()

    @classmethod
    def imageWithFilePath_(cls, filepath):
        return NSImage.alloc().initWithContentsOfFile_(filepath)

    def writeToFilePath_(self, filepath):
        self.lockFocus()
        image_rep = NSBitmapImageRep.alloc().initWithFocusedViewRect_(self.rect())
        self.unlockFocus()
        representation = _getFileRepresentationType(filepath)
        data = image_rep.representationUsingType_properties_(representation, None)
        data.writeToFile_atomically_(filepath, False)

    def fillWithColor_(self, color):
        self.lockFocus()
        color.set()
        NSBezierPath.fillRect_(self.rect())
        self.unlockFocus()


    
