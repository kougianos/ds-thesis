import sys

# Disable __pycache__ folder creation
sys.dont_write_bytecode = True
sys.path.append('./test_folder')
import printHello as Ph

Ph.hello_world()
