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
# 10 G connection for dcswitch 66 67.58.51.135

servers = ["67.58.51.135:/mnt/disk1", "67.58.51.135:/mnt/disk2"\
           "67.58.51.136:/mnt/disk1", "67.58.51.136:/mnt/disk2"\
           "67.58.51.137:/mnt/disk1", "67.58.51.135:/mnt/disk2"\
           "67.58.51.138:/mnt/disk1", "67.58.51.138:/mnt/disk2"\
           "67.58.51.139:/mnt/disk1", "67.58.51.139:/mnt/disk2"\
           "67.58.51.140:/mnt/disk1", "67.58.51.140:/mnt/disk2"\
           "67.58.51.141:/mnt/disk1", "67.58.51.141:/mnt/disk2"\
           "67.58.51.142:/mnt/disk1", "67.58.51.142:/mnt/disk2"\
           "67.58.51.143:/mnt/disk1", "67.58.51.143:/mnt/disk2"\
           "67.58.51.144:/mnt/disk1", "67.58.51.144:/mnt/disk2"\
           "67.58.51.145:/mnt/disk1", "67.58.51.145:/mnt/disk2"\
           "67.58.51.146:/mnt/disk1", "67.58.51.146:/mnt/disk2"\
           "67.58.51.147:/mnt/disk1", "67.58.51.147:/mnt/disk2"\
           "67.58.51.148:/mnt/disk1", "67.58.51.148:/mnt/disk2"\
           "67.58.51.149:/mnt/disk1", "67.58.51.149:/mnt/disk2"\
           "67.58.51.150:/mnt/disk1", "67.58.51.150:/mnt/disk2"\
           "67.58.51.151:/mnt/disk1", "67.58.51.151:/mnt/disk2"\
           "67.58.51.152:/mnt/disk1", "67.58.51.152:/mnt/disk2"\
           "67.58.51.153:/mnt/disk1", "67.58.51.153:/mnt/disk2"\
           "67.58.51.154:/mnt/disk1", "67.58.51.154:/mnt/disk2"\
           "67.58.51.155:/mnt/disk1", "67.58.51.155:/mnt/disk2"\
           "67.58.51.156:/mnt/disk1", "67.58.51.156:/mnt/disk2"\
           "67.58.51.157:/mnt/disk1", "67.58.51.157:/mnt/disk2"\
           "67.58.51.158:/mnt/disk1", "67.58.51.158:/mnt/disk2"\
           "67.58.51.134:/mnt/disk1", "67.58.51.134:/mnt/disk2"\
]


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
    if(empty() == False):
      print "Directory is not empty"
      # copyFile("random_number_file_ID_0.txt", servers[0], "/mnt/disk1")
      path = "/home/dsrikant/rdrand-number-generator/output" 
      filelist = sorted(os.listdir(path))
      for currFile in sorted(filelist):
        # Keep all our storage disks at 95 ish capacity
        # Consider using a transferred folder here?
        if int(gotRoomAgain(servers[dest])) > 95:
          dest += 1
        if str(currFile).endswith('.txt'):
           copyFile(currFile, servers[dest]) 
    else:
      print "Directory is empty"
      time.sleep(300) # Sleep for 300 seconds


# Call driver
transfer()
