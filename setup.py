from distutils.core import setup
import py2exe, sys, os

if len(sys.argv) == 1:
    sys.argv.append("py2exe")

setup(
    options = {'py2exe': {
                        'bundle_files': 2,
                        "includes":["tkinter"]
                        }
               },
    zipfile = None,
    windows = [{"script": 'appli.py'}]
)
