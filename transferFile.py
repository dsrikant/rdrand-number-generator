import os
import socket
import random

# Send the file to the proper dcswitch server
# Servers 66 to 90
# Fill in the rest of the servers.
# Pass along ssh keys to the rest of dcswitch
servers = ["dcswitch66", "dcswitch67", "dcswitch68"] 


def copyFile(file_to_copy, dest_server, disk):
  send = "scp output/" + file_to_copy + " " + dest_server + ":" + disk 
  os.system(send)
  remove = "rm output/" + file_to_copy
  os.system(remove)  

# /mnt/disk1
# /mnt/disk2

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

def empty():
  path = '/home/dsrikant/rdrand-number-generator' 
  if os.listdir(path) == []: 
    return True
  else:
    return False

def transfer():
  while True:
    if(empty() == False): # Need a good number here
      print "Directory is not empty"
      # copyFile("random_number_file_ID_0.txt", servers[0], "/mnt/disk1") 
      copyFile(random.choice(os.listdir("output/")), servers[0], "/mnt/disk1") 
    else:
      print "Directory is empty"
      time.sleep(300) # Sleep for 300 seconds


transfer()
