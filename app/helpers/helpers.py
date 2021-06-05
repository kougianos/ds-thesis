import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
from pymongo import MongoClient


def open_file_name():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tk.Tk().withdraw()
    filename = askopenfilename(initialdir=dir_path)
    return filename


def get_mongo_client():
    return MongoClient(
        open('helpers/credentials'))
