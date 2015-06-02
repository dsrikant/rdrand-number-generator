import os
import sys

#with open('random_number_file_ID_5636.txt') as f:
with open('8_kibibytes.txt') as f:
  head = [next(f) for x in xrange(10)]

p = repr(head[0])
p.rstrip()
tmp = p.split('\\x')
print len(head[0])
print head
print head[0]

del tmp[0]
del tmp[len(tmp) - 1]
del tmp[len(tmp) - 2]
del tmp[len(tmp) - 3]

ind = 0

#print ord(head[0])

#for i in head[0]:
#  for char in i:
#    print char
#  print hex(ord(i))
 # ind += 1
#  print str(ind)

for i in head:
    for j in i:
#        print ord(j)
        ind+=1

print ind
