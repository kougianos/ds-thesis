import pandas as pd


def dataframe_details(dataframe):
    lines = dataframe.shape[0]
    columns = dataframe.shape[1]
    total_elements = int(dataframe.size)
    null_elements = dataframe.isna().sum().sum()
    descr = dataframe.describe().to_dict()
    pass


# Read data to dataframe
df = pd.read_csv('test_folder/student-merged.csv')

# Get descriptive statistics from dataframe as dict
descr_to_dict = df.describe().to_dict()
descr_to_dict = dataframe_details(df)

# Get specific column of dataframe to list
g1 = df['G1']
g1_list = g1.tolist()

pass
