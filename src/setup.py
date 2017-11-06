__author__ = 'sledg_000'

from cx_Freeze import setup, Executable
import sys
from _version import __version__

sys.argv.append("build")
#main
exe = Executable(script="main.py", icon="main.ico", base="Win32GUI")#, compress=True
buildOptions = dict(excludes = ["tkinter", "PyQt4.uic"], includes =["queue", "requests", "idna.idnadata","PyQt4"], optimize=1)
setup(name = "main",version = _version, description = "Remote Object Backup", executables = [exe], options = dict(build_exe = buildOptions))


if __name__ == "__main__":
    pass