#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="arc")
ttk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()

