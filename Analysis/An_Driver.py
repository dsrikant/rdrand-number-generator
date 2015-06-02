import os

#def move():
    # Move the file with the sorted data to the scratch server

#def divvy():
    # Split up the work amongst five servers for starters
    # Maybe get more clever and split up the work between all the servers that sent files

def q_sort():

    with open('res.txt') as f:
        array = f.readlines()

    l = []
    e = []
    g = []

    if len(array) > 1:
        p = array[0]
    for x in array:
      if x < p:
        l.append(x)
      if x == p:
        e.append(x)
      if x > p:
        g.append(x)
    return q_sort(l)+e+q_sort(g)
  else:    
    return array

def filter()
    # Run Analysis on every "full" disk
    path = "/mnt/disk1"
    filelist = sorted(os.listdir(path))
    for cf in sorted(filelist):
        #cmd = "./a.out 8_kikibytes.txt"
        # Remember to remove the verified file.
        if "hashed" not in str(currFile)
            # Generate a file called res.txt with all the valid number
            # for our current iteration
            cmd = "./a.out " + cf
            os.system(cmd)
    # QuickSort res.txt, still need to test my implementation so I haven't called
    # it yet.

    # Send result of quicksort to dcswitch90 for 
