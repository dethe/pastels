'''
    Minimalist build file for pastels.py

    To build run 'python setup.py py2app' on the command line
'''

NAME = "Pastels"
SCRIPT = "PastelsView.py"
VERSION = "0.3"
ID = "pastels"
COPYRIGHT = "Copyright 2005, 2006 Dethe Elza"
DATA_FILES = []


from setuptools import setup
setup(
    plugin=[SCRIPT],
    setup_requires=["py2app"],
    options=dict(
        py2app=dict(
            extension=".saver",
            plist = dict(
                CFBundleIdentifier = 'org.livingcode.plugins.pastels',
                CFBundleShortVersionString = ' '.join([NAME, VERSION]),
                CFBundleName = NAME,
                NSHumanReadableCopyright = COPYRIGHT,
                NSPrincipalClass = 'PastelsView',
            )
        )
    )
)

#from setuptools import setup

#
#plist = dict(
#    NSPrincipalClass='PastelsView',
#    CFBundleName     = NAME,
#    CFBundleShortVersionString = ' '.join([NAME, VERSION]),
#    CFBundleGetInfoString = NAME,
#    CFBundleIdentifier = 'org.livingcode.applications.%s' % ID,
#    NSHumanReadableCopyright = COPYRIGHT,
#)
#
#
#setup(
#    setup_requires=['py2app'],
#    plugin=['PastelsView.py'],
#    options=dict(
#        py2app=dict(
#            extension='.saver',
#            plist=plist,
#        )
#    ),
#)

