import sys

sys.dont_write_bytecode = True
from helpers import helpers as h

username = 'defaultUser'

h.print_init_cli()
lang = h.get_user_preferred_language()
h.print_welcome_cli(lang)

functionality = h.get_user_selected_functionality_cli(lang)

if functionality == 1:
    username = h.get_user_name(lang)
    # TODO
elif functionality == 2:
    df, filename = h.get_user_dataframe(lang)
    h.ask_user_destination_folder_and_save_excels(df, filename, lang)
else:
    pass

pass
