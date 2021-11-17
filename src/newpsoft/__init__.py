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

if platform.system().lower() == "windows":
    cmd_pre = ["start", "cmd.exe", "/c"]
    cmd_post = ["^&", "pause"]
else:
    cmd_pre = ["xdg-open"]
    cmd_post = []

class Meeper:
    python = None
    pythonw = None
    def __init__(self, filename, executable=None):
        if not Meeper.python or not Meeper.pythonw:
            Meeper.python = find_python()
            Meeper.pythonw = find_pythonw()
        self.exe = executable if executable else Meeper.python if filename.endswith(".py") else Meeper.pythonw
        self.filename = filename

    def meep(self):
        subprocess.call(cmd_pre + [self.exe, self.filename] + cmd_post, shell=True)

