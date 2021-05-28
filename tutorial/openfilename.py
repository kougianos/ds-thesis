import tkinter as tk
from tkinter.filedialog import askopenfilename
import os

# Current directory the script is placed
dir_path = os.path.dirname(os.path.realpath(__file__))

tk.Tk().withdraw()

fn = askopenfilename(initialdir=dir_path)
print(fn)
f = open(fn, 'r')
print(f.read())