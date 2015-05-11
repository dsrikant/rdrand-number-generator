import os
import socket
import random
import glob
import time
import subprocess

# Send the file to the proper dcswitch server
# Servers 66 to 90
# Fill in the rest of the servers.
# Pass along ssh keys to the rest of dcswitch
# Add the rest of the available file paths here...
servers = ["dcswitch66:/mnt/disk1"]#, "dcswitch66:/mnt/disk2", "dcswitch67:/mnt/disk1", "dcswitch68"] 


def copyFile(file_to_copy, dest):
  send = "scp output/" + file_to_copy + " " + dest 
  os.system(send)

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
  dest = 0
  while True:
    print "dest = " + str(dest)
    if(empty() == False):
    #  print "Directory is not empty"
      # copyFile("random_number_file_ID_0.txt", servers[0], "/mnt/disk1")
      path = "/home/dsrikant/rdrand-number-generator/output" 
      filelist = sorted(os.listdir(path))
      for currFile in sorted(filelist):
        # Keep all our storage disks at 95 ish capacity
        print "dest again : " + str(dest)
        print int(gotRoomAgain(servers[dest]))
        if int(gotRoomAgain(servers[dest])) > 95:
          dest += 1
        if str(currFile).endswith('.txt'):
           copyFile(currFile, servers[dest]) 
    else:
      print "Directory is empty"
      time.sleep(300) # Sleep for 300 seconds


# Call driver
transfer()
