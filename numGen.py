# This runs the ./rdrand executable

# Figure out a file size to do, may not be done in this script

import os
import time
import hashlib
import datetime

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
    return name

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
    # For an output file with 5G of random numbers
    # ./rdrand --size=5000000k --output=testout.txt
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
  while True:
    if(directorySize() < 100000): # Need a good number here, or use directory size code
      timeBefore = datetime.datetime.now() 
      currFile = newFile(curr_file_ID) 
      timeAfter = datetime.datetime.now() 
      # Don't like the output of this, verify correct usage...?
      fd = os.open( currFile, os.O_RDWR|os.O_CREAT )
      os.fsync(fd)
      hashFileName = hashFile(currFile, hashThis(currFile + '.txt'))
      curr_file_ID += 1
      coreTemp = recordCoreTemp()
      toWrite = "Filename : " + currFile + ",  HashedFile Name : " + hashFileName\
                + ",  CoreTemp : " + coreTemp + ",  Start Time : " + str(timeBefore)\
                + ",  End Time : " + str(timeAfter) + "\n"
      f = open('/home/dsrikant/rdrand-number-generator/CryptoDiagnostics.txt', "a")
      f.write(toWrite)
      f.close()
    else:
      # May need to increase this number so more files can be transferred?
      time.sleep(5)   


# Call driver
numGen()

