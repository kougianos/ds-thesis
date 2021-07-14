import sys
import pandas as pd

sys.dont_write_bytecode = True
from helpers import helpers as h

h.welcome_screen()

file = h.open_file_name()

df = pd.read_csv(file)

details_df = h.get_dataframe_general_info(df)
h.save_dataframe_to_excel(details_df, 'test')
pass
