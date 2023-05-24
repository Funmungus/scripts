import glob
import os
import newpsoft
import sys
import subprocess
import tkinter as tk

fpath = os.getcwd()
allpyfiles = []
allpywfiles = []
window = False
buttons = []

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
        button = tk.Button(window, text=os.path.basename(i), command=newpsoft.Meeper(i).meep)
        button.pack(pady=4)
        buttons.append(button)
    for i in allpywfiles:
        button = tk.Button(window, text=os.path.basename(i), command=newpsoft.Meeper(i).meep)
        button.pack(pady=4)
        buttons.append(button)

def main():
    global fpath
    global window
    for i in sys.argv[::-1]:
        if os.path.isdir(i):
            fpath = i
            break
    if not fpath:
        fpath = os.getcwd()
    window = tk.Tk()
    window.title("Scripts")
    button = tk.Button(window, text="Reload", command=reload)
    button.pack(pady=(32, 32))
    reload()
    window.update_idletasks()
    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    w, h = window.winfo_width() + 32, window.winfo_height() + 32
    x, y = sw - w, sh - h - 200
    window.geometry(f'{w}x{h}+{x}+{y}')
    window.mainloop()

if __name__ == "__main__":
    main()

