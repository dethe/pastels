'''
    Minimalist build file for pastels.py

    To build run 'python setup.py py2app' on the command line
'''

from distutils.core import setup
import py2app

plist = dict(
    NSPrincipalClass='PastelsView',
    CFBundleName='Pastels',
)

setup(
    plugin=['PastelsView.py'],
    options=dict(py2app=dict(
        extension='.saver',
        plist=plist,
    )),
)

