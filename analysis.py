import os
import sys

with open('random_number_file_ID_5636.txt') as f:
  head = [next(f) for x in xrange(10)]

p = repr(head[2])
p.rstrip()
tmp = p.split('\\x')
print len(head[0])
print head

del tmp[0]
del tmp[len(tmp) - 1]
del tmp[len(tmp) - 2]
del tmp[len(tmp) - 3]

ind = 0

for i in tmp:
  for char in i:
    print char
    print hex(ord(char))
  ind += 1
  print str(ind)
