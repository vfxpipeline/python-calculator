import sys
from distutils.core import setup
import py2exe
from PyQt4 import QtGui
from ui.main import Ui_MainWindow


sys.path.append('C:\\Windows\\WinSxS\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.30729.6161_none_50934f2ebcb7eb57')

excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
            "pywin.dialogs", "pywin.dialogs.list"]

setup(
        name="Python Calculator",
        version="1.0",
        description="A demo software from VFX Pipeline",
        author="Rajiv Sharma",
        author_email="rajiv@technicaldirector.in",
        url="http://technicaldirector.in",
        copyright="Copyright (c) 2015 www.technicaldirector.in",
        license="End-user License Agreement (EULA)",
        options={"py2exe": {"typelibs":
                  [ ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 0, 1, 2)],
                  "compressed": 1,
                  "optimize": 2,
                  'bundle_files': 1,
                  "excludes": excludes,
                  'dll_excludes': ["IPHLPAPI.DLL", "NSI.dll",  "WINNSI.DLL",  "WTSAPI32.dll"],
                  "includes": ["sip", "PyQt4"]}},
        zipfile=None,
        windows=[
            {
                "script": "calculator.py",
                "icon_resources": [(1, "calculator.ico")],
                "copyright":"(c) www.technicaldirector.in"
            }
            ],
        data_files=[]
)
