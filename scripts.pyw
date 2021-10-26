import glob
import os
import sys
import subprocess
import tkinter as tk

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

fpath = os.path.dirname(__file__)
python = find_python()
pythonw = find_pythonw()
allpyfiles = []
allpywfiles = []
window = False
buttons = []

class Meeper:
    def __init__(self, filename):
        self.exe = python if filename.endswith(".py") else pythonw
        self.filename = filename

    def meep(self):
        subprocess.call(["start", "cmd.exe", "/c", self.exe, self.filename, "^&", "pause"], shell=True)

def reload():
    global allpyfiles
    global allpywfiles
    global window
    global buttons
    allpyfiles = glob.glob(os.path.join(fpath, "*.py"))
    allpywfiles = glob.glob(os.path.join(fpath, "*.pyw"))
    if __file__ in allpyfiles:
        allpyfiles.remove(__file__)
    if __file__ in allpywfiles:
        allpywfiles.remove(__file__)
    if not window:
        return
    for i in buttons:
        i.destroy()
    for i in allpyfiles:
        button = tk.Button(window, text=os.path.basename(i), command=Meeper(i).meep)
        button.pack()
        buttons.append(button)
    for i in allpywfiles:
        button = tk.Button(window, text=os.path.basename(i), command=Meeper(i).meep)
        button.pack()
        buttons.append(button)

def main():
    global window
    window = tk.Tk()
    window.title("Scripts")
    button = tk.Button(window, text="Reload", command=reload)
    button.pack()
    reload()
    window.mainloop()

if __name__ == "__main__":
    main()

