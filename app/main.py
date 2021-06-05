import sys

sys.dont_write_bytecode = True
from helpers import helpers as h

client = h.get_mongo_client()
file = h.open_file_name()
pass
