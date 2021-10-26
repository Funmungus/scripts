import os
import subprocess
import sys

def find_python():
    python = os.path.dirname(sys.executable)
    canbes = ["python3", "python3.exe", "python", "python.exe"]
    for i in canbes:
        pyte = os.path.join(python, i)
        if os.path.isfile(pyte):
            return pyte
    return sys.executable
python = find_python()

def install(package):
    subprocess.check_call([python, "-m", "pip", "install", "--upgrade", package])

if __name__ == '__main__':
    install('ttkthemes')
    install('evdev')
    install('python-uinput')
