# Helper methods to be used from main python script
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox, Label, X
import os
import pandas as pd
from pymongo import MongoClient


def open_file_name():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tk.Tk().withdraw()
    filename = askopenfilename(initialdir=dir_path, title='Select which file to open')
    return filename


def get_mongo_client():
    return MongoClient(open('helpers/mongocredentials'))


def dataframe_details(dataframe):
    details = dataframe.describe().to_dict()
    details_df = pd.DataFrame(details)
    return details_df


def get_dataframe_general_info(dataframe):
    general_info_dict = {
        'lines': [dataframe.shape[0]],
        'columns': [dataframe.shape[1]],
        'total_elements': [int(dataframe.size)],
        'null_elements': [int(dataframe.isna().sum().sum())]
    }
    info_df = pd.DataFrame(general_info_dict, index=['count'])
    info_df = info_df.T

    return info_df


def save_dataframe_to_excel(dataframe, filename):
    directory = get_directory()
    dataframe.to_excel(directory + '/' + filename + '.xlsx', index=True, header=True)


def get_directory():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tk.Tk().withdraw()
    directory = askdirectory(initialdir=dir_path, title='Select where to save the file')
    return directory


def welcome_screen():
    top = tk.Tk()
    calibri_font = 'Calibri 11'

    button_frame = tk.Frame(top)
    button_frame.pack(fill=tk.X, side=tk.BOTTOM)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    def end_program():
        top.destroy()
        exit(1)

    # get screen width and height
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    width = 450
    height = 300
    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    top.geometry('%dx%d+%d+%d' % (width, height, x, y))

    top.title("Welcome Screen")
    label_middle = Label(
        top,
        text=welcome_text(),
        wraplength=400,
        font=calibri_font,
    )
    label_middle.pack(ipady=30)

    exit_button = tk.Button(
        button_frame,
        text="Exit",
        fg='red',
        command=end_program,
        font=calibri_font,
    )

    continue_button = tk.Button(
        button_frame,
        text="Continue",
        command=top.destroy,
        font=calibri_font,
    )

    exit_button.grid(row=0, column=0, sticky=tk.W + tk.E)
    continue_button.grid(row=0, column=1, sticky=tk.W + tk.E)

    top.mainloop()


# TODO
def welcome_text():
    return '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
    laborum. '''
