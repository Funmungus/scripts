import os
import platform
import sys
import subprocess
from . import auto

def find_python():
    python = os.path.dirname(sys.executable)
    canbes = ["python3", "python3.exe", "python", "python.exe"]
    for i in canbes:
        pyte = os.path.join(python, i)
        if os.path.isfile(pyte):
            return pyte
    return sys.executable

def find_pythonw():
    python = os.path.dirname(sys.executable)
    canbes = ["pythonw", "pythonw.exe"]
    for i in canbes:
        pyte = os.path.join(python, i)
        if os.path.isfile(pyte):
            return pyte
    return sys.executable

class Meeper:
    python = None
    pythonw = None
    def __init__(self, filename, executable=None, window=None):
        if not Meeper.python or not Meeper.pythonw:
            Meeper.python = find_python()
            Meeper.pythonw = find_pythonw()
        self.exe = executable if executable else Meeper.python if filename.endswith(".py") else Meeper.pythonw
        self.filename = filename
        self.window = window

    def meep(self):
        if self.window:
            self.window.withdraw()
        subprocess.call([self.exe, self.filename])
        # subprocess.call(cmd_pre + [self.exe, self.filename] + cmd_post, shell=True)

        if self.window:
            self.window.state("normal")
            self.window.lift()
