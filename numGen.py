# This runs the ./rdrand executable

# Figure out a file size to do, may not be done in this script

import os
cmd = './rdrand --size=8k --output=8_kibibytes.txt'
os.system(cmd) # returns the exit status
