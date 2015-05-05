# This runs the ./rdrand executable

# Figure out a file size to do, may not be done in this script

import os
import time
import hashlib

# Call the rdrand instruction
# For each filename increment this counter.
# Generate files of size somewhere between 1G and 10G


# Find the shasum of the file
def hashThis(filename):
  func = hashlib.sha256()
  f = open(filename, 'rb')
  try:
    func.update(f.read())
  finally:
    f.close()
  return func.digest()



# Create a new file with the hash of current file
def hashFile(currFile, hashValue):
  name = currFile + '_hashed.txt'

  try:
    print(name)
    file = open(name,'w+')
    file.write(hashValue)
    file.close()

  except:
    print('Something is up here')




# Run rdrand instruction
def newFile(ID):
    cmd = './rdrand --size=8k --output=random_number_file_ID_' + str(ID) + '.txt'
    os.system(cmd) # returns the exit status
    return 'random_number_file_ID_' + str(ID)



# Loop "infinitely", stop at 2 for testing right now
# Or until certain sizeof directory
def numGen():
  curr_file_ID = 0;
    #while(directory(some_path, '.txt'))
  while(curr_file_ID < 2):
    currFile = newFile(curr_file_ID) 
    # This value needs to be updated as we generate bigger and bigger files
    time.sleep(2)
    hashFile(currFile, hashThis(currFile + '.txt'))
    curr_file_ID += 1
     


# Call driver
numGen()






## Some things I was messing around with, leaving them around for now.


# Grabbing core temp
# Checking if this is accurate?
# Code from ... , make any necessary modifications
# Most likely don't need to, since it's just a diagnostic.
# https://pypi.python.org/pypi/PySensors/
# Doesn't work yet
'''import sensors

sensors.init()
try:
    for chip in sensors.iter_detected_chips():
        print '%s at %s' % (chip, chip.adapter_name)
        for feature in chip:
            print '  %s: %.2f' % (feature.label, feature.get_value())
finally:
    sensors.cleanup()'''


