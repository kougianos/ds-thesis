import pandas as pd

# Read data to dataframe
df = pd.read_csv('test_folder/student-merged.csv')

# Get descriptive statistics from dataframe as dict
descr_to_dict = df.describe().to_dict()

# Get specific column of dataframe to list
g1 = df['G1']
g1_list = g1.tolist()

pass
