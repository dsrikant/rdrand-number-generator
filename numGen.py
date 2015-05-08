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



def recordCoreTemp():
   f = open('/sys/class/thermal/thermal_zone0/temp');
   temp = f.read();
   f.close()
   print(temp);

   # write this to our log file?
   return temp


# Run rdrand instruction
def newFile(ID):
    # Need to remember to increase the file size here.
    cmd = './rdrand --size=8k --output=output/random_number_file_ID_' + str(ID) + '.txt'
    os.system(cmd) # returns the exit status
    return 'output/random_number_file_ID_' + str(ID)

# Get size of output folder
# http://snipplr.com/view/47686/
def directorySize():
  source = "output/"
  total_size = os.path.getsize(source)
  for item in os.listdir(source):
    itempath = os.path.join(source, item)
    if os.path.isfile(itempath):
      total_size += os.path.getsize(itempath)
    elif os.path.isdir(itempath):
      total_size += _total_size(itempath)
  return total_size


# Loop "infinitely", stop at 2 for testing right now
# Or until certain sizeof directory
def numGen():
  curr_file_ID = 0;
    #while(directory(some_path, '.txt'))
  while True:
    if(directorySize() < 100000):
      currFile = newFile(curr_file_ID) 
      # This value needs to be updated as we generate bigger and bigger files
      #time.sleep(2)
      fd = os.open( currFile, os.O_RDWR|os.O_CREAT )
      os.fsync(fd)
      hashFile(currFile, hashThis(currFile + '.txt'))
      curr_file_ID += 1
      recordCoreTemp()
    else:
      time.sleep(100)   


# Call driver
numGen()

