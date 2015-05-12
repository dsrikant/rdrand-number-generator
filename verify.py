# Run this on dcswitch

# Check for runs of zeros
# Open a file?
import filecmp
import time
import os
import sys
import hashlib

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
  name = currFile + '_hashed_verification.txt'

  try:
    #print(name)
    file = open(name,'w+')
    file.write(hashValue)
    file.close()
    return name

  except:
    print('Something is up here')



# Still need a clever way to figure out which files are on the server running
# the instance of this script
def verify():
  while True:                                                                      
      path = "/mnt/disk1"
      filelist = sorted(os.listdir(path))
      for currFile in sorted(filelist):
        if "hashed" not in str(currFile) and "verified" not in str(currFile) and str(currFile).endswith('.txt') and str(currFile) not in open('verified.txt').read():
          sp = currFile.split(".")
          print currFile
          hash_verify = hashThis(currFile)
          hash_file_verify = hashFile(sp[0], hash_verify)
          while True: # Reconsider this while true
            if not os.path.isfile(sp[0] + "_hashed.txt"):
              time.sleep(3)
            else:
              checksum = filecmp.cmp(sp[0] + "_hashed.txt", hash_file_verify)
              # Hanging if checksum not verified?
              if checksum:
                f = open("verified.txt", "a")
                f.write(currFile + "\n")
                f.close()
                remove1 = "ssh crypto rm /home/dsrikant/rdrand-number-generator/output/" + currFile 
                remove2 = "ssh crypto rm /home/dsrikant/rdrand-number-generator/output/" + sp[0] 
                remove3 = "ssh crypto rm /home/dsrikant/rdrand-number-generator/output/" + sp[0] + "_hashed.txt" 
                os.system(remove1)
                os.system(remove2)
                os.system(remove3)
                break

verify()
