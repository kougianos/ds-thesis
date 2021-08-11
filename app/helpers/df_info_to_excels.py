import sys

import pandas as pd

sys.dont_write_bytecode = True
import helpers as h

df1 = pd.read_csv('../data/datatest.csv')
df2 = pd.read_csv('../data/datatest2.csv')
df3 = pd.read_csv('../data/datatraining.csv')

df1_general_info = h.get_dataframe_general_info(df1)
df2_general_info = h.get_dataframe_general_info(df2)
df3_general_info = h.get_dataframe_general_info(df3)

df1_details = h.get_dataframe_details(df1)
df2_details = h.get_dataframe_details(df2)
df3_details = h.get_dataframe_details(df3)

h.save_dataframe_to_excel(df1_general_info, 'datatest_info', False)
h.save_dataframe_to_excel(df2_general_info, 'datatest2_info', False)
h.save_dataframe_to_excel(df3_general_info, 'datatraining_info', False)
h.save_dataframe_to_excel(df1_details, 'datatest_details', False)
h.save_dataframe_to_excel(df2_details, 'datatest2_details', False)
h.save_dataframe_to_excel(df3_details, 'datatraining_details', False)
