'''
    Minimalist build file for pastels.py

    To build run 'python setup.py py2app' on the command line
'''

from setuptools import setup

plist = dict(
    NSPrincipalClass='PastelsView',
    CFBundleName='Pastels',
)

setup(
    setup_requires=['py2app'],
    plugin=['PastelsView.py'],
    options=dict(py2app=dict(
        extension='.saver',
        plist=plist,
    )),
)

