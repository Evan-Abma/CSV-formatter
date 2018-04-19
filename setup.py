import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'c:/Anaconda/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'c:/Anaconda/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = ["os", "numpy", "pandas", "tkinter", "csv", "datetime"],
    excludes = [],
    include_files=['c:/Anaconda/DLLs/tcl86t.dll', 'c:/Anaconda/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('tkintertest.py', base=base)
]

setup(name='tkintertest',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)