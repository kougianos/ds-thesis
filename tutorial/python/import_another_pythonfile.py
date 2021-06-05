import sys

sys.dont_write_bytecode = True              # Disable __pycache__ folder creation, should always be on top
sys.path.append('test_folder')            # Import test folder in system path
from tutorial.python.test_folder import printHello as Ph
from open_file_name import open_file_name   # Import file from same directory
from python_mongo import get_mongo_client

Ph.hello_world()
open_file_name()
mongoClient = get_mongo_client()
