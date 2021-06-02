import sys

sys.dont_write_bytecode = True              # Disable __pycache__ folder creation
sys.path.append('./test_folder')            # Import test folder in system path
from test_folder import printHello as Ph    # Different directory
from open_file_name import open_file_name   # Same directory

Ph.hello_world()
open_file_name()
