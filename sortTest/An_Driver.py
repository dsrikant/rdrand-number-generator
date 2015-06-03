import os

def q_sort(array):
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


with open('data.txt') as f:
  array = f.readlines()

res = q_sort(array)

f = open('dcswitch66_sorted.txt','a')

for j  in res:
  f.write(j)

f.close()
