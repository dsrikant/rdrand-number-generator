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
    print(name)
    file = open(name,'w+')
    file.write(hashValue)
    file.close()
    return name

  except:
    print('Something is up here')



# Still need a clever way to figure out which files are on the server running
# the instance of this script
def verify():                                                                          
      path = "/mnt/disk1"
      filelist = sorted(os.listdir(path))
      for currFile in sorted(filelist):
        if "hashed" not in str(currFile) and str(currFile).endswith('.txt'):
          sp = currFile.split(".")
          hash_verify = hashThis(currFile)
          hash_file_verify = hashFile(sp[0], hash_verify)
          while True:
            if not os.path.isfile(sp[0] + "_hashed.txt"):
              time.sleep(3)
            else:
              checksum = filecmp.cmp(sp[0] + "_hashed.txt", hash_file_verify)

              if checksum:
                remove1 = "ssh dcswitch66 rm /home/dsrikant/rdrand-number-generator/output/" + currFile 
                remove2 = "ssh dcswitch66 rm /home/dsrikant/rdrand-number-generator/output/" + sp[0] 
                remove3 = "ssh dcswitch66 rm /home/dsrikant/rdrand-number-generator/output/" + sp[0] + "_hashed.txt" 
                os.system(remove1)
                os.system(remove2)
                os.system(remove3)


verify()
