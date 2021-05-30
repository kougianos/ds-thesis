import tkinter as tk
from tkinter.filedialog import askopenfilename
import os


def open_file_name():
    # Current directory the script is placed
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tk.Tk().withdraw()

    filename = askopenfilename(initialdir=dir_path)
    return filename
