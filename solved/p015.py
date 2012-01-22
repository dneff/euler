#!/usr/bin/python
# Dan Neff - (dan@neff.cc)
# Starting in the top left corner of a 2x2 grid, 
# there are 6 routes (without backtracking) to the bottom right corner.
#
# How many routes are there through a 20x20 grid? 
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
# correction -- where any number is less than N.
#
# doh. pascal triangle!
#

import math,sys

grid_length = 20

triangle = [1]

def iterate_triangle(x):
  new_list = [1]
  for i in range(0,len(x)):
    if i == len(x) - 1:
      new_list.append(x[-1])
      return new_list
    new_list.append((x[i] + x[i + 1]))

for x in range(0,(grid_length * 2)):
  triangle = iterate_triangle(triangle)

print sorted(list(set(triangle)))[-1]
