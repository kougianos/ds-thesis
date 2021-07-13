# Helper methods to be used from main python script
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
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
