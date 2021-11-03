import os
import subprocess
import sys
import scripts
import platform

python = scripts.find_python()

def install(package):
    subprocess.check_call([python, "-m", "pip", "install", "--upgrade", package])

if __name__ == '__main__':
    install('ttkthemes')
    install('opencv-contrib-python')
    install('Pillow')
    if platform.system().lower() != "windows":
        install('evdev')
        install('python-uinput')
