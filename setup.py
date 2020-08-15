#!/usr/bin/env python3

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

if __name__ == '__main__':
    install('ttkthemes')
    install('evdev')
    install('python-uinput')
