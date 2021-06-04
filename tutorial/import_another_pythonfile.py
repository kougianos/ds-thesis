import sys

sys.dont_write_bytecode = True              # Disable __pycache__ folder creation
sys.path.append('./test_folder')            # Import test folder in system path
from test_folder import printHello as Ph    # Import file from different directory
from open_file_name import open_file_name   # Import file from same directory
from python_mongo import get_mongo_client

Ph.hello_world()
open_file_name()
mongoClient = get_mongo_client()
