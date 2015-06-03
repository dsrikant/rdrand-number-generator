import sys
import os

# to run on all files stored on dcswitch90
#path = ''
#fl = sorted(os.listdir(path))


with open('dcswitch66_sorted.txt') as f:
  tmp = f.readlines()

med = int(tmp[len(tmp)/2])
q1 = int(tmp[len(tmp)/4])
q2 = int(tmp[(3*len(tmp))/4])

print q1
print med
print q2

# Open up the rest of the files
#with open('dcswitch66_sorted.txt') as f:

# For now just work with tmp
lq1 = open('lq1.txt', 'a')
q1_med = open('q1_med.txt', 'a')
med_q2 = open('med_q2.txt', 'a')
gq2 = open('gq2.txt', 'a')


# Make five files ehre for the values
for i in tmp:
  if int(i) < q1:
    lq1.write(i + '\n')
  elif int(i) >= q1 and int(i) < med:
    q1_med.write(i + '\n')
  elif int(i) >= med and int(i) < q2:
    med_q2.write(i + '\n')
  elif int(i) >= q2:
    gq2.write(i + '\n')

lq1.close()
q1_med.close()
med_q2.close()
gq2.close()

#for cf in fl:
  # Do your clever sorting here

