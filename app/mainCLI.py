import sys

sys.dont_write_bytecode = True
from helpers import helpers as h

h.print_init_cli()
lang = h.get_user_preferred_language()
h.print_welcome_cli(lang)

functionality = h.get_user_selected_functionality_cli(lang)

# Functionality 1 is to execute a selected algorithm to the predefined datasets and save results to MongoDB
# Functionality 2 is to open any dataset and create 2 excel files containing information
# Functionality 3 is to retrieve algorithm executions from online MongoDB cluster and save results to excel file
if functionality == 1:
    results = dict()
    results['username'] = h.get_user_name(lang)
    selected_algorithm = h.get_user_selected_algorithm(lang)
    results.update(h.execute_user_selected_algorithm(selected_algorithm, lang))
    h.save_results_to_mongodb(results, lang)
elif functionality == 2:
    df, filename = h.get_user_dataframe(lang)
    h.ask_user_destination_folder_and_save_excels(df, filename, lang)
elif functionality == 3:
    results_df = h.get_mongo_algorithm_executions(lang)
    h.save_dataframe_to_excel(results_df, 'algorithm_executions', True, lang=lang)

# For .exe file only
# if lang == 'EN':
#     print('Press any key to end program...')
# else:
#     print('Πατήστε οποιοδήποτε πλήκτρο για να τερματιστεί το πρόγραμμα...')
#
# x = input()
