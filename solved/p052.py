#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# It can be seen that the number, 125874, and its double, 
# 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x
# contain the same digits.
#
import math,sys


def int2array(x):
  return list(str(x))

def array2int(x):
  return int(('').join(x))

x = 0
search = True

while search:
  if len(int2array(x)) < len(int2array(x * 6)):
    x = 10**len(int2array(x))
  else:
    x += 1
  if (x % 2 == 0) or (x % 5 == 0):
    continue
  if len(int2array(x)) > len(set(int2array(x))):
    continue

  for multiplier in range(2,7):
    y = x * multiplier
    if sorted(int2array(x)) != sorted(int2array(y)):
      break
    if multiplier == 6:
      search = False

print 'solution: ',x
