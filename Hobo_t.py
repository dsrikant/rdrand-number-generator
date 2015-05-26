import os
import socket
import random
import glob
import time
import subprocess
import hashlib

# Send the file to the proper dcswitch server
# Servers 66 to 90
# Fill in the rest of the servers.
# Pass along ssh keys to the rest of dcswitch
# Add the rest of the available file paths here...
# 10 G connection for dcswitch 66 67.58.51.135

servers = ["67.58.51.150:/mnt/disk1"]

servers.append("67.58.51.150:/mnt/disk2")
servers.append("67.58.51.151:/mnt/disk1")
servers.append("67.58.51.151:/mnt/disk2")
servers.append("67.58.51.152:/mnt/disk1")
servers.append("67.58.51.152:/mnt/disk2")
servers.append("67.58.51.153:/mnt/disk1")
servers.append("67.58.51.153:/mnt/disk2")
servers.append("67.58.51.154:/mnt/disk1")
servers.append("67.58.51.154:/mnt/disk2")
servers.append("67.58.51.155:/mnt/disk1")
servers.append("67.58.51.155:/mnt/disk2")
servers.append("67.58.51.156:/mnt/disk1")
servers.append("67.58.51.156:/mnt/disk2")
servers.append("67.58.51.157:/mnt/disk1")
servers.append("67.58.51.157:/mnt/disk2")
servers.append("67.58.51.158:/mnt/disk1")
servers.append("67.58.51.158:/mnt/disk2")
servers.append("67.58.51.134:/mnt/disk1")
servers.append("67.58.51.134:/mnt/disk2")


def hashThis(filename):
  print "In hashThis"
  func = hashlib.md5()
  f = open(filename, 'rb')
  try:
    func.update(f.read())
  finally:
    f.close()
  return func.digest()


def hashFile(currFile, hashValue):
  print "In hashFile"
  
  temp = currFile.split('.')

  name = temp[0] + '_hashed.txt'

  try:
    print(name)
    file = open(name,'w+')
    file.write(hashValue)
    file.close()
    return name

  except:
    print "something is up here"

def copyFile(file_to_copy, dest):
  print "Copying to : " + str(dest)
  # Hash the file then copy it over
  hashFileName = hashFile( "output/" + file_to_copy, hashThis("output/" + file_to_copy))
  print "HashFile name is : " + hashFileName
  toWrite = "File : " + file_to_copy + " Destination : " + dest + "\n"
  f = open('HoboTransfers.txt', "a")
  f.write(toWrite)
  f.close()
  send = "scp output/" + file_to_copy + " " + dest 
  send2 = "scp " + hashFileName + " " + dest 
  os.system(send)
  os.system(send2)
  

# /mnt/disk1
# /mnt/disk2

# Get the percentage of disk space available on current dcswitch
def gotRoomAgain(destination):
  parts = destination.split(":")
  host = parts[0]
  cmd = "df -hT " + parts[1]

  ssh = subprocess.Popen(["ssh", "%s" % host, cmd],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
  result = str(ssh.stdout.readlines())
  arr = result.split("%")
  
  #This is the percent usage
  return arr[1][-2:]


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

# Is the output folder empty?
def empty():
  path = '/home/dsrikant/rdrand-number-generator/output' 
  if os.listdir(path) == []: 
    return True
  else:
    return False



def transfer():
  # index in server array so we can check file capacity
  #dest = 0
  # Move this up to 1 becasue I ahd to re start the pipeline
  # after the first disk is full
  #dest = 1
  dest = 0
  while True:
    if(empty() == False):
#      print "Directory is not empty"
      # copyFile("random_number_file_ID_0.txt", servers[0], "/mnt/disk1")
      path = "/home/dsrikant/rdrand-number-generator/output" 
      filelist = sorted(os.listdir(path))
      for currFile in sorted(filelist):
        # Keep all our storage disks at 95 ish capacity
        # Consider using a transferred folder here?
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if int(gotRoomAgain(servers[dest])) > 95:
          dest += 1
          if dest >= len(servers):
            sys.exit(0)
        temp = currFile.split('_')
        oe = int(temp[4]) % 2
        if oe != 0 :
            print "Odd Baby"
        if str(currFile).endswith('.txt') and str(currFile) in open("CryptoDiagnostics.txt").read() and str(currFile) not in open("HoboTransfers.txt").read() and "hashed" not in str(currFile):
           print "Transferring File : " + str(currFile)
           #copyFile(currFile, servers[dest]) 
    else:
      print "Directory is empty"
      time.sleep(60) # Sleep for 300 seconds

# Call driver
transfer()
