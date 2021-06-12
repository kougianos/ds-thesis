import pandas as pd


def dataframe_details(dataframe):
    info_dict = {
        'lines': dataframe.shape[0],
        'columns': dataframe.shape[1],
        'total_elements': int(dataframe.size),
        'null_elements': int(dataframe.isna().sum().sum())
    }
    descr = dataframe.describe().to_dict()
    descr_df = pd.DataFrame(descr)
    descr_df.to_csv('df.csv', index=True, header=True)
    pass


# Read data to dataframe
df = pd.read_csv('test_folder/student-merged.csv')

# Get descriptive statistics from dataframe as dict
df_details = dataframe_details(df)

# Get specific column of dataframe to list
g1 = df['G1']
g1_list = g1.tolist()

pass
