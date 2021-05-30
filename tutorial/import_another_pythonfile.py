import sys

# Disable __pycache__ folder creation
sys.dont_write_bytecode = True
sys.path.insert(1, './')
import tutorial.test_folder.printHello as Ph

Ph.hello_world()
