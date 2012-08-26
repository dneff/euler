#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
#
# A common security method used for online banking is to ask the user for
# three random characters from a passcode. For example, if the passcode was
# 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
# reply would be: 317.
#
# The text file, p079-keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown length.
#
# In the shortest case, all digits appear once. Let's try for that first...
#
import math,sys,string,itertools

def int2array(x):
  return list(str(x))

def array2int(x):
  return int(('').join(x))

def validcombokey(key,combo):
  while combo:
    if combo[0] == key[0]:
      combo.pop(0)
      key.pop(0)
    else:
      combo.pop(0)
    if len(key) == 0:
      return True
  return False

fh = open('./p079-keylog.txt','r')

keys = map(string.strip,fh.readlines())

keys = [int2array(x) for x in sorted(set(keys))]

uniques = sorted(set([x for key in keys for x in key]))

for combo in itertools.permutations(uniques):
  solution = True
  for key in keys:
    if not validcombokey(list(key),list(combo)):
      solution = False
      break
  if solution:
    print 'solution: ', ('').join(combo)

