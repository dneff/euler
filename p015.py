#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# Starting in the top left corner of a 2x2 grid, 
# there are 6 routes (without backtracking) to the bottom right corner.
#
# How many routes are there through a 20x20 grid? 
#
#
# This one stumped me for a bit, until clued into 
# on a 2x2 you'll always go right twice (RR) and 
# down twice (DD), so we're just working through
# combinations of D and R across 40 steps.
# 
# co-worker's insight after discussion
#
# strategy-- a 40 position binary and count every
# combination where there's an equal number of 1'
# and 0's (substituting for D's and R's)...
#
# hmmm. this would find the right answer, but not
# any time soon. Rethinking...
#
# insight -- for a grid of NxN, the question is equivalent
# to "How many ways can you sum numbers that equal 2N?"
#
#
#
import math,sys

def bitlist(number,size):
  if number.bit_length() > size:
    print "Error: number needs more bits than size specified"
    sys.exit(1)
  bits = '{0:0' + str(size) + 'b}'
  return list(bits.format(number))

grid_width = 20

path_count = 0

i = 1

while i:
  right = 0
  down = 0
  test_path = bitlist(i,(2*grid_width))
  for node in test_path:
    if int(node) == 0:
      right += 1
    if int(node) == 1:
      down += 1
  if right == down:
    path_count += 1
    print test_path
    print path_count
  i = i + 1
