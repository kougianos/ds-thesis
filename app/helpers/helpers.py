# Helper methods to be used from main python scripts
import datetime
import json
import os
import tkinter as tk
import tkinter.messagebox
from tkinter import Label
from tkinter.filedialog import askopenfilename, askdirectory

import cpuinfo
import pandas
import pandas as pd
import psutil
from pymongo import MongoClient
from sklearn import svm, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier


def open_file_name() -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    filename = askopenfilename(initialdir=dir_path, title='Select which file to open')
    return filename


def get_mongo_client() -> MongoClient:
    return MongoClient(open('data/mongocredentials'))


def get_dataframe_details(dataframe: pandas.DataFrame) -> pandas.DataFrame:
    details = dataframe.describe().to_dict()
    details_df = pd.DataFrame(details)
    return details_df


def get_dataframe_general_info(dataframe: pandas.DataFrame) -> pandas.DataFrame:
    general_info_dict = {
        'lines': [dataframe.shape[0]],
        'columns': [dataframe.shape[1]],
        'total_elements': [int(dataframe.size)],
        'null_elements': [int(dataframe.isna().sum().sum())]
    }
    info_df = pd.DataFrame(general_info_dict, index=['count'])
    info_df = info_df.T

    return info_df


def save_dataframe_to_excel(dataframe: pandas.DataFrame, filename: str, askfordir: bool = True,
                            directory: str = '.', lang='EN') -> None:
    if askfordir:
        directory = get_directory()
        dataframe.to_excel(directory + '/' + filename + '.xlsx', index=True, header=True)
    else:
        dataframe.to_excel(directory + '/' + filename + '.xlsx', index=True, header=True)

    if lang == 'EN':
        print("Excel file saved successfully!")
    else:
        print("Το αρχείο excel σώθηκε επιτυχώς!")


def get_directory() -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tk.Tk().withdraw()
    directory = askdirectory(initialdir=dir_path, title='Select where to save the file(s)')
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
        text=welcome_text_tkinter(),
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
def welcome_text_tkinter() -> str:
    return '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
    laborum. '''


def get_processor_name() -> str:
    return cpuinfo.get_cpu_info()['brand_raw']


def get_size(bytez, suffix="B") -> str:
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytez < factor:
            return f"{bytez:.2f}{unit}{suffix}"
        bytez /= factor


def get_total_memory() -> str:
    mem = psutil.virtual_memory()
    return get_size(mem.total)


def get_user_preferred_language() -> str:
    while True:
        try:
            lang = int(input())
        except ValueError:
            print("Wrong input. Valid inputs: 1 or 2")
            continue
        else:
            if lang not in [1, 2]:
                print("Wrong input. Valid inputs: 1 or 2")
                continue
            if lang == 1:
                print('Your selected language is English')
                return "EN"
            else:
                print('Η επιλεγμένη γλώσσα είναι τα ελληνικά')
                return "GR"


def print_init_cli():
    f = open('text/initCLI.txt', encoding="utf8")
    print(f.read())


def print_welcome_cli(lang: str = 'EN'):
    f = open('text/welcomeCLI_' + lang + '.txt', encoding="utf8")
    print(f.read())


def get_user_selected_functionality_cli(lang: str = 'EN') -> int:
    if lang == 'EN':
        wrong_input = "Wrong input. Valid inputs: 1, 2 or 3"
    else:
        wrong_input = "Λάθος επιλογή. Έγκυρες επιλογές: 1, 2 ή 3"
    while True:
        try:
            choice = int(input())
        except ValueError:
            print(wrong_input)
            continue
        else:
            if choice not in [1, 2, 3]:
                print(wrong_input)
                continue
            return choice


def get_user_name(lang: str = 'EN') -> str:
    f = open('text/functionality1_username_' + lang + '.txt', encoding="utf8")
    print(f.read())
    username = input()
    if username == '':
        username = 'defaultUser'
    msg = 'Username: ' + username
    print(msg)
    return username


def get_user_dataframe(lang: str = 'EN'):
    f = open('text/functionality2_' + lang + '.txt', encoding="utf8")
    print(f.read())
    while True:
        filename = open_file_name()
        if '.csv' not in filename:
            if filename == '':
                exit(1)
            if lang == 'EN':
                err = 'ERROR: File does not have .csv extension. Please open another file'
                print(err)
                show_tkinter_errorbox('ERROR', err)
                continue
            else:
                err = 'ΣΦΑΛΜΑ: Το αρχείο δεν έχει επέκταση .csv. Παρακαλώ επιλέξτε άλλο αρχείο'
                print(err)
                show_tkinter_errorbox('ΣΦΑΛΜΑ', err)
                continue
        break
    return pd.read_csv(filename), str.replace(filename, '.csv', '').rpartition('/')[2]


def ask_user_destination_folder_and_save_excels(dataframe: pandas.DataFrame, filename: str, lang: str = 'EN'):
    f = open('text/functionality2_end_' + lang + '.txt', encoding="utf8")
    print(f.read().replace('$DATASET$', filename))
    directory = get_directory()
    if directory == '':
        exit(1)
    df_info = get_dataframe_general_info(dataframe)
    df_details = get_dataframe_details(dataframe)
    save_dataframe_to_excel(df_info, filename + '_info', False, directory, lang=lang)
    save_dataframe_to_excel(df_details, filename + '_details', False, directory, lang=lang)


def show_tkinter_messagebox(title: str, msg: str):
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    tkinter.messagebox.showinfo(title, msg, parent=root)


def show_tkinter_errorbox(title: str, msg: str):
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    tkinter.messagebox.showerror(title, msg, parent=root)


def get_user_selected_algorithm(lang: str = 'EN') -> str:
    choice = 0
    f = open('text/functionality1_algorithm_' + lang + '.txt', encoding="utf8")
    print(f.read())
    if lang == 'EN':
        wrong_input = "Wrong input. Valid inputs: 1, 2, 3 or 4"
    else:
        wrong_input = "Λάθος επιλογή. Έγκυρες επιλογές: 1, 2, 3 ή 4"
    while True:
        try:
            choice = int(input())
        except ValueError:
            print(wrong_input)
            continue
        else:
            if choice not in [1, 2, 3, 4]:
                print(wrong_input)
                continue
            break

    algorithms_tuple = ('SVM', 'Logistic Regression', 'Naive Bayes', 'Decision Tree')
    selected_algorithm = algorithms_tuple[choice - 1]
    msg = 'Algorithm: ' + selected_algorithm
    print(msg)
    return selected_algorithm


def execute_user_selected_algorithm(selected_algorithm: str, lang: str = 'EN') -> dict:
    df1 = pd.read_csv('data/datatest.csv').drop(['sn', 'date'], axis=1)
    df2 = pd.read_csv('data/datatest2.csv').drop(['sn', 'date'], axis=1)
    df_train = pd.read_csv('data/datatraining.csv').drop(['sn', 'date'], axis=1)
    df_test = df1.append(df2)
    x_train = df_train.iloc[:, 0:5]
    x_test = df_test.iloc[:, 0:5]
    y_train = df_train['Occupancy']
    y_test = df_test['Occupancy']
    clf = None
    results = dict()

    if selected_algorithm == 'SVM':
        clf = svm.SVC(kernel='linear')
    elif selected_algorithm == 'Logistic Regression':
        clf = LogisticRegression(solver='lbfgs')
    elif selected_algorithm == 'Naive Bayes':
        clf = GaussianNB()
    elif selected_algorithm == 'Decision Tree':
        clf = DecisionTreeClassifier()

    if lang == 'EN':
        print(selected_algorithm + ' execution in progress...')
    else:
        print('Ο αλγόριθμος ' + selected_algorithm + ' βρίσκεται σε εκτέλεση...')

    results['algorithmExecuted'] = selected_algorithm
    results['executedOn'] = str(datetime.datetime.now())
    results['cpu'] = get_processor_name()
    results['ram'] = get_total_memory()
    results['isCharging'] = str(psutil.sensors_battery().power_plugged)
    begin_time = datetime.datetime.now()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    f1_score = metrics.f1_score(y_test, y_pred)

    results['accuracy'] = str(accuracy)
    results['precision'] = str(precision)
    results['recall'] = str(recall)
    results['f1'] = str(f1_score)

    completion_time = datetime.datetime.now() - begin_time
    results['executionTime'] = str(completion_time)

    if lang == 'EN':
        print(selected_algorithm + ' execution finished successfully!')
    else:
        print('Ο αλγόριθμος ' + selected_algorithm + ' εκτελέστηκε επιτυχώς!')

    return results


def save_results_to_mongodb(results: dict, lang: str = 'EN') -> str:
    if lang == 'EN':
        print('Saving results to MongoDB...')
    else:
        print('Αποθήκευση αποτελεσμάτων στην MongoDB...')

    mongo_client = get_mongo_client()
    algorithms_db = mongo_client.get_database('algorithmsDb')
    algorithms_collection = algorithms_db.get_collection('algorithmsCollection')
    insert_result = algorithms_collection.insert_one(results)
    doc_id = str(insert_result.inserted_id)

    if lang == 'EN':
        print('MongoDB document successfully inserted. ID: ' + doc_id)
    else:
        print('Επιτυχημένη αποθήκευση στην MongoDB. ID: ' + doc_id)
    print(json.dumps(results, indent=4, sort_keys=False, default=str, ensure_ascii=False))
    return doc_id


def get_mongo_algorithm_executions(lang: str = 'EN') -> pandas.DataFrame:
    f = open('text/functionality3_' + lang + '.txt', encoding="utf8")
    print(f.read())
    mongo_client = get_mongo_client()
    algorithms_db = mongo_client.get_database('algorithmsDb')
    algorithms_collection = algorithms_db.get_collection('algorithmsCollection')
    results = list(algorithms_collection.find({}, {"_id": 0}))
    df = pd.DataFrame(results, columns=["username", "algorithmExecuted", "executedOn", "cpu", "ram", "isCharging",
                                        "accuracy", "precision", "recall", "f1", "executionTime"])
    print("MongoDB retrieve: DONE")
    return df
